import sys


def main():
    with open(sys.argv[1], 'r') as f:
        a = list(map(int, f.readlines()))
    median = sorted(a)[len(a) // 2]
    print(sum(abs(x - median) for x in a))


if __name__ == '__main__':
    main()
