import sys

def main():
    if sys.argv[1] == "--help" or "-h":
        print("\033[1mTakes 2 arguments:\033[0m")
        print("a, b")
        return

    args = sys.argv[1:]
    
    a = int(args[0])
    b = int(args[1])
    c = a
    sum = 0

    while c <= b:
        if c % 2 == 1:
            sum += c
        c += 1
    
    print(sum)

if __name__ == "__main__":
    main()


