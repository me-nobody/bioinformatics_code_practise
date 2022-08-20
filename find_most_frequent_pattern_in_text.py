from types import NoneType

filename = "rosalind_ba1d.txt"
def find_substrings(filename = None, k =0):
    """to find overlapping occurences of pattern in text, use the sliding window approach. loop over the length of the text in multiples of query
       sequence length starting from 0 to len(text)-len(pattern) and check if the string matches. find the most
       frequent pattern
    """
    # get some sequence data
    with open(filename) as input_file:
        data = input_file.readlines()

    # create a file to write into
    #output_file = open("Documents/Datascience_Project/bioinformatics_code_practise/output_file.txt","w")

    # input the length of the k-mer
    #k = 3
    idx = 0
    # the query sequence is given in the second line of the text file from rosalind
    dna_seq = str(data[1]).strip()
    # create a list to store the list of substrings
    sub_string_array=[]
    for idx in range(len(dna_seq)-(idx+k)):
        # it is important select the search length same as pattern length
        # sliding window to search for overlapping patterns
        sub_string = dna_seq[idx:idx+k]
        sub_string_array.append(sub_string)      
    return sub_string_array, dna_seq

def count_substrings(filename = None,k = 0):
    # call find_substrings with filename and k-mer value and collect substring array and DNA sequence
    sub_string_array, dna_seq = find_substrings(filename,k)
    # convert the list of k-mers to a dictionary and set initial count to zero
    sub_string_dict = dict.fromkeys(sub_string_array,0)
    idx = 0
    for key in sub_string_dict:
        # for each substring iterate along the length of the DNA sequence
        for idx in range(len(dna_seq)-idx+k):
            pattern = dna_seq[idx:idx+k]
            if key == pattern:
                sub_string_dict[key] = sub_string_dict[key] + 1   # increment the count when substring in dictionary
    print(sub_string_dict)                                        # matches the pattern of the sliced DNA sequence
count_substrings(filename,3)
