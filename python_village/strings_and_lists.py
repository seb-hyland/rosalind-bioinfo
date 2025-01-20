import sys

def main():
    if sys.argv[1] == "--help" or "-h":
        print("\033[1mTakes 5 arguments:\033[0m")
        print("s, a, b, c, d")
        return

    args = sys.argv[1:]
    
    string = args[0]
    slice1 = string[int(args[1]):int(args[2]) + 1]
    slice2 = string[int(args[3]):int(args[4]) + 1]
    
    print(f'{slice1} {slice2}')

if __name__ == "__main__":
    main()

