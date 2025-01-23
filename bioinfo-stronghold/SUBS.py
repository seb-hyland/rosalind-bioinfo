import sys


def main():
    s = sys.argv[1]
    t = sys.argv[2]

    if len(t) > len(s):
        print("substring t is longer than s")

    matches = []
    i = 0
    while i <= len(s) - len(t):
        if t[0] == s[i]:
            subseq = s[i:i+len(t)]
            if subseq == t:
                matches.append(i+1)
        i += 1

    print(" ".join(map(str, matches)))


if __name__ == "__main__":
    main()


