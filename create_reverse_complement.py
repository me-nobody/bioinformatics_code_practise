"""we use string translate with dictionary to get reverse complement"""
import sys
def reverse_complement(file_name):
    # read file contents
    with open(file_name,"r") as fh:
        dna_seq = fh.read()
        dna_seq = dna_seq.upper().strip()
    # create a dictionary with characters encoded as ASCII code
    base_dict = {65:84,84:65,67:71,71:67}    
    complement = dna_seq.translate(base_dict)
    reverse_comp = complement[::-1]
    print(dna_seq[:10].strip())    
    print(reverse_comp[-10:])

if __name__ == "__main__":
    print("please provide the input file")
    # other way is to use i,arg in enumerate(sys.argv)
    if len(sys.argv) == 2:
        # collect the file name in a variable
        file_name = sys.argv[1]
        # run the program
        reverse_complement(file_name)
    else:
        print(f"no file found, only {sys.argv[0]} program found")    
