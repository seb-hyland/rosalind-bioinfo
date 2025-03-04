import sys

def main() -> None:
    s: str = sys.argv[1]
    freq_dict: dict[str, int] = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1

    print(" ".join(map(str, freq_dict.values())))


if __name__ == "__main__":
    main()

