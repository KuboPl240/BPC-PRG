import pytest
from pathlib import Path
import numpy as np
import matplotlib

import assignment_8_1 as hw


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ('load_sequence', True),
        ('count_matches', True),
        ('compute_matrix', True),
        ('plot_matrix', True),
        ('main', True),
    ]
)
def test_attributes(string, expected):
    assert hasattr(hw, string)


@pytest.mark.parametrize(
    ("file_name", "start_idx", "stop_idx", "expected_nt"),
    [
        ("input_data/sequence01.txt", 0, 1, "A"),
        ("input_data/sequence01.txt", 10, 11, "C"),
        ("input_data/sequence01.txt", 123, 124, "A"),
        ("input_data/sequence01.txt", 0, 51, "ATGGGGACTGCAGCTGCGGCAGCGGCGGCGGCGGCGGCGGCGGCGGCCGGG"),
        ("input_data/sequence01.txt", 654, 720, "AACAACCCGTCCAGTCAGAGAGCCCTCTGCCTGTGCCTGGTACTCCTGGCCGTGCTCGGCTGCAGC"),
        ("input_data/sequence02.txt", 0, 1, "A"),
        ("input_data/sequence02.txt", 10, 11, "G"),
        ("input_data/sequence02.txt", 123, 124, "A"),
        ("input_data/sequence02.txt", 0, 51, "ATGGCTGTTGGCCAGATTGGAAACTTCCTGGCTTACACGGCGGTCCCCACG"),
        ("input_data/sequence02.txt", 654, 720, "ATGGCCTGTGGATTCACGACCGTCTCCGTGGGGATTGTCCTTATACAGGTGTTCAAAGAGTTCAAT"),
    ]
)
def test_load_sequence(file_name, start_idx, stop_idx, expected_nt):
    seq = hw.load_sequence(Path(file_name))
    if file_name == "input_data/sequence01.txt":
        assert len(seq) == 990
    else:
        assert len(seq) == 765
    assert seq[start_idx:stop_idx] == expected_nt


@pytest.mark.parametrize(
    ("seq1", "seq2", "expected_match_count"),
    [
        ("AAAAA", "CCCCC", 0),
        ("ACGT", "ACGT", 4),
        ("GCTAGTCAGATCTGACGC", "GATGGTCACATCTGCCGC", 14),
        ("GTCAGAT", "GGTCACT", 2),
    ]
)
def test_count_matches(seq1, seq2, expected_match_count):
    assert hw.count_matches(seq1, seq2) == expected_match_count


@pytest.mark.parametrize(
    ("seq1", "seq2", "window_size", "match_count"),
    [
        ("AAAA", "CCCCC", 3, 1),
        ("ACGT", "ACGT", 2, 1),
        ("GCTAGTCAGATCTGACGC", "GATGGTCACATCTGCCGC", 5, 3),
        ("GTCAGAT", "GGTCACT", 3, 3),
        ("GTCAGAT", "GGTCA", 3, 2),
        ("GTCAGAT", "GGTCA", 1, 1)
    ]
)
def test_compute_matrix(seq1, seq2, window_size, match_count):
    expected_matrix = np.load('test_files/compute_matrix_w_' + str(window_size) + '_m_' + str(match_count) + '.npy')
    assert np.all(hw.compute_matrix(seq1, seq2, window_size, match_count) == expected_matrix)


@pytest.mark.parametrize(
    ("window_size", "match_count"),
    [
        (5, 3),
        (7, 3),
        (1, 1),
        (10, 8),
        (20, 12)
    ]
)
def test_main(window_size, match_count):
    matplotlib.use('Agg')
    matrix = hw.main(Path("input_data/sequence01.txt"), Path("input_data/sequence01.txt"), window_size, match_count)

    assert np.shape(matrix) == (990, 990)
    assert np.all(matrix == np.load('test_files/main_w_' + str(window_size) + '_m_' + str(match_count) + '.npy'))
