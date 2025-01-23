import sys


def main():
    k = float(sys.argv[1])
    m = float(sys.argv[2])
    n = float(sys.argv[3])
    p = k + m + n

    Pr_kk = (k/p) * ((k-1)/(p-1))
    Pr_km = (k/p) * (m/(p-1)) + (m/p) * (k/(p-1))
    Pr_kn = (k/p) * (n/(p-1)) + (n/p) * (k/(p-1))
    Pr_mm = (m/p) * ((m-1)/(p-1))
    Pr_mn = (m/p) * (n/(p-1)) + (n/p) * (m/(p-1))

    Pr = Pr_kk*1 + Pr_km*1 + Pr_kn*1 + Pr_mm*0.75 + Pr_mn*0.5

    print(Pr)


if __name__ == "__main__":
    main()

