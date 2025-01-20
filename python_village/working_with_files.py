import sys

def main():
    if sys.argv[1] == "--help" or "-h":
        print("\033[1mTakes 1 argument:\033[0m")
        print("The path to the file")
        print("\033[1mNotes:\033[0m")
        print("The file will be modified in place")
        return

    file = sys.argv[1]
    output_vector = []
    
    with open(file, 'r') as file_read:
        for id, line in enumerate(file_read):
            line_number = id + 1
            if line_number % 2 == 0:
                output_vector.append(line)
    
    with open(file, 'w') as file_write:
        file_write.writelines(output_vector)


if __name__ == "__main__":
    main()

