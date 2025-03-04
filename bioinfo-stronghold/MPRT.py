import sys
from urllib.request import urlopen


def main():
    ids = sys.argv[1].split()

    for id in ids:
        try:
            url = f'http://www.uniprot.org/uniprot/{id}.fasta' 
            print("-----")
            page = urlopen(url)
            contents = page.read()
            print(contents)
            page.close()
        except Exception as e:
            print(f'Failed to access page {id} due to {e}')


if __name__ == "__main__":
    main()

