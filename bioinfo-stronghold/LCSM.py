import sys


def main():
    s = sys.argv[1]

    cur_seq = ""
    sequences = []
    longest_sequence = ""

    for line in s.splitlines():
        if line.startswith('>'):
            if cur_seq != "":
                sequences.append(cur_seq)
                cur_seq = ""
        else:
            cur_seq += line.strip()

    sequences.append(cur_seq)

    for i in range(0, len(sequences[0])):
        if len(sequences[0]) - i <= len(longest_sequence):
            break
        ss = greatest_subseq(i, sequences)
        if len(ss) > len(longest_sequence):
            longest_sequence = ss

    print("\n\n----------------\n\n")
    print(longest_sequence)


def greatest_subseq(idx, sequences):
    best_match = ""
    ss_len = 1
    while idx + ss_len <= len(sequences[0]):
        cur_seq = sequences[0][idx:idx+ss_len]
        ss_len += 1
        for i in range(1, len(sequences)):
            if cur_seq not in sequences[i]:
                return best_match
        best_match = cur_seq
    return best_match

        
if __name__ == "__main__":
    main()

