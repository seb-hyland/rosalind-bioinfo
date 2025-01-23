import sys


def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    c = 3

    # Caches the 2nd last, last, and current result
    cache = {
        -2: None,
        -1: 1,
        0: 1,
    }
    
    while c <= n:
        cache[-2] = cache[-1]
        cache[-1] = cache[0]
        cache[0] = k*cache[-2]+cache[-1]
        c += 1
        
    print(cache[0])


if __name__ == "__main__":
    main()



