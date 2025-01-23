import sys


def main():
    s = sys.argv[1]
    t = sys.argv[2]

    distance = 0
    for s_char, t_char in zip(s, t):
        if s_char is not t_char:
            distance += 1

    print(distance)


if __name__ == "__main__":
    main()


