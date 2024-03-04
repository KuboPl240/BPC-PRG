# READ TXT FILE:
with open (r"C:\Users\Jakub\Documents\BPC-PRG\lecture5\my_sequence.txt", "r") as txt_file:
    dna_string = txt_file.read()

# YOUR CODE HERE:
    dna_length = len(dna_string)
    index = 0
    dna_segmented= []
    segment_range = []
    while len(dna_string)>0:
        end_of_seqence = dna_string.find('TGA')
        dna_segmented.append(dna_string[:end_of_seqence])
        dna_string = dna_string[end_of_seqence+3:]
        segment_range.append([index,end_of_seqence+index])
        index = index+end_of_seqence
    print(dna_segmented)
    print(segment_range)