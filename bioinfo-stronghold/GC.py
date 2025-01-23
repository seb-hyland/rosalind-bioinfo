import sys


def main():
    s = sys.argv[1]

    cur_id = None;
    cur_seq = "";
    highest_gc = (None, 0.0)

    for line in s.splitlines():
        if line.startswith('>'):
            if cur_id is not None:
                cur_gc = get_gc(cur_seq)
                if cur_gc > highest_gc[1]:
                    highest_gc = (cur_id, cur_gc)

            cur_id = line[1::]
            cur_seq = ""

        else:
            cur_seq += line.strip()

    cur_gc = get_gc(cur_seq)
    if cur_gc > highest_gc[1]:
        highest_gc = (cur_id, cur_gc)

    print(f'{highest_gc[0]}\n{highest_gc[1]*100}')


def get_gc(s):
    count = sum(1 for c in s if c in 'GC')
    return float(count) / float(len(s)) if len(s) > 0 else 0.0


if __name__ == "__main__":
    main()

