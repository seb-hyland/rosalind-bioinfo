import sys

def main():
    if sys.argv[1] == "--help" or "-h":
        print("\033[1mTakes 2 arguments:\033[0m")
        print("a and b")
        return

    args = sys.argv[1:]
    x = int(args[0])
    y = int(args[1])
    print(x**2 + y**2)

if __name__ == "__main__":
    main()

