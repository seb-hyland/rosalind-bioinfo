import sys


def main():
    AA_AA = float(sys.argv[1])
    AA_Aa = float(sys.argv[2])
    AA_aa = float(sys.argv[3])
    Aa_Aa = float(sys.argv[4])
    Aa_aa = float(sys.argv[5])
    aa_aa = float(sys.argv[6])
    p = AA_AA + AA_Aa + AA_aa + Aa_Aa + Aa_aa + aa_aa
    
    P1 = AA_AA / p
    P2 = AA_Aa / p
    P3 = AA_aa / p
    P4 = Aa_Aa / p
    P5 = Aa_aa / p
    P6 = aa_aa / p
    
    Pr = P1*1 + P2*1 + P3*1 + P4*0.75 + P5*0.5 + P6*0
    total = Pr * p * 2
    print(total)


if __name__ == "__main__":
    main()

