import sys

def main():
    if sys.argv[1] == "--help" or "-h":
        print("\033[1mTakes 1 argument:\033[0m")
        print("s")
        print("\033[1mNotes:\033[0m")
        print("It is advised to wrap s in quotation marks to pass it as a single argument")
        return

    s = sys.argv[1]
    dictionary = {}
    
    for word in s.split():
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    for word, count in dictionary.items():
        print(f'{word} {count}')


if __name__ == "__main__":
    main()


