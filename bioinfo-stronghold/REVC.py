import sys


def main():
    s = sys.argv[1]
    s_rev = s[::-1]
    complement_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    
    print("".join(complement_map.get(c, '_') for c in s_rev))


if __name__ == "__main__":
    main()

