import sys


def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    cache = {
        0: 0,
        1: 1,
    }

    for _ in range(3, n + 1):
        # Every rabbit that doesn't die makes a new rabbit
        new_generation = sum(cache.get(i, 0) for i in range(1, m))
        # Every rabbit ages by 1 year
        for i in range(m-1, 0, -1):
            cache[i] = cache.get(i-1, 0)
        cache[0] = new_generation

    alive = sum(cache.get(i, 0) for i in range(0, m))
    print(alive)


if __name__ == "__main__":
    main()
