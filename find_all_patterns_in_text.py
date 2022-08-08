filename = "Documents/Datascience_Project/bioinformatics_code_practise/rosalind_ba1d.txt"
def find_all_patterns(filename):
    """to find overlapping occurences of pattern in text, use the sliding window approach. loop over the length of the text in multiples of query
       sequence length starting from 0 to len(text)-len(pattern) and check if the string matches
    """
    # get some sequence data
    with open(filename) as input_file:
        data = input_file.readlines()

    # create a file to write into
    output_file = open("Documents/Datascience_Project/bioinformatics_code_practise/output_file.txt","w")

    # pattern is given in the first line of the text file from rosalind    
    pattern = str(data[0]).strip()  # strip had to be added as pattern text had extra spaces
    
    # the query sequence is given in the second line of the text file from rosalind
    dna_seq = str(data[1]).strip()
    
    for idx in range(len(dna_seq)-len(pattern)):
        # it is important select the search length same as pattern length
        # sliding window to search for overlapping patterns
        sub_string = dna_seq[idx:idx+len(pattern)]        
        if sub_string == pattern:
            
            output_file.write(str(idx))
            output_file.write("\n")
    output_file.close()        

find_all_patterns(filename)    