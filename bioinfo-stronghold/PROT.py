import sys


def main():
    s = sys.argv[1]
    i = 0
    out = ""

    codon_dict = {
        "UUU": "F",      
        "CUU": "L",      
        "AUU": "I",      
        "GUU": "V",
        "UUC": "F",      
        "CUC": "L",      
        "AUC": "I",      
        "GUC": "V",
        "UUA": "L",      
        "CUA": "L",      
        "AUA": "I",      
        "GUA": "V",
        "UUG": "L",      
        "CUG": "L",      
        "AUG": "M",      
        "GUG": "V",
        "UCU": "S",      
        "CCU": "P",      
        "ACU": "T",      
        "GCU": "A",
        "UCC": "S",      
        "CCC": "P",      
        "ACC": "T",      
        "GCC": "A",
        "UCA": "S",      
        "CCA": "P",      
        "ACA": "T",      
        "GCA": "A",
        "UCG": "S",      
        "CCG": "P",      
        "ACG": "T",      
        "GCG": "A",
        "UAU": "Y",      
        "CAU": "H",      
        "AAU": "N",      
        "GAU": "D",
        "UAC": "Y",      
        "CAC": "H",      
        "AAC": "N",      
        "GAC": "D",
        "UAA": "Stop",   
        "CAA": "Q",      
        "AAA": "K",      
        "GAA": "E",
        "UAG": "Stop",   
        "CAG": "Q",      
        "AAG": "K",      
        "GAG": "E",
        "UGU": "C",      
        "CGU": "R",      
        "AGU": "S",      
        "GGU": "G",
        "UGC": "C",      
        "CGC": "R",      
        "AGC": "S",      
        "GGC": "G",
        "UGA": "Stop",   
        "CGA": "R",      
        "AGA": "R",      
        "GGA": "G",
        "UGG": "W",      
        "CGG": "R",      
        "AGG": "R",      
        "GGG": "G",       
    }


    while i < len(s):
        codon = s[i:i+3]
        sym = codon_dict.get(codon, "_")
        if sym != "Stop":
            out += sym
        else:
            break
        i += 3
    print("\n\n----------\n\n")
    print(out)



if __name__ == "__main__":
    main()

