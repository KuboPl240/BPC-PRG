import pytest
import assignment_9_1 as hw


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("read_file", True),
        ("names_to_dict", True),
        ("frequency_counter", True),
        ("main", True),
    ]
)
def test_attributes(string, expected):
    assert hasattr(hw, string)


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("test.txt", ["Cras", "purus", "nibh", "aliquet", "sed", "volutpat", "non"]),
    ]
)
def test_read(string, expected):
    assert hw.read_file(string) == expected


@pytest.mark.parametrize(
    ("list_of_names", "expected"),
    [
        ([], {}),
        (
            ["Adam", "Boris", "Erika", "Rut", "Viola"],
            {"A": ["Adam"], "B": ["Boris"], "E": ["Erika"], "R": ["Rut"], "V": ["Viola"]}
        ),
        (
            ["Adam", "Alena", "Alik"],
            {"A": ["Adam", "Alena", "Alik"]}
        ),
    ]
)
def test_to_dict(list_of_names, expected):
    assert hw.names_to_dict(list_of_names) == expected


@pytest.mark.parametrize(
    ("classroom", "expected"),
    [
        ([], {}),
        (["Alena", "Boris", "Borivoj", "Blanka", "Tereza", "Tibor", "Viola"], {"A": 1, "B": 3, "T": 2, "V": 1}),
        (["Cecilie", "Ctibor", "Cindy"], {"C": 3}),
    ]
)
def test_counter(classroom, expected):
    assert hw.frequency_counter(classroom) == expected


@pytest.mark.parametrize(
    ("classroom", "expected"),
    [
        (["Boris", "Tereza", "Borivoj", "Blanka",  "Viola", "Tibor", "Vanda"], {"B": 3, "T": 2, "V": 2}),
    ]
)
def test_anticounter(classroom, expected):
    """Testuje nespravnost vysledku pri binarnim vyhledavani na neserazenem seznamu."""
    assert hw.frequency_counter(classroom) != expected


def test_docstring():
    assert hw.read_file.__doc__
    assert hw.names_to_dict.__doc__
    assert hw.frequency_counter.__doc__
    assert hw.main.__doc__
