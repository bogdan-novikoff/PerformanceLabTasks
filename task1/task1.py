import sys


def main():
    n, m = map(int, sys.argv[1:])

    assert n >= 1, f"n = {n}, ожидалось, что n >= 1"
    assert m >= 1, f"m = {m}, ожидалось, что m >= 1"

    if m == 1:
        print(1)
        return

    cur = 1
    print(cur, end='')
    while True:
        cur = (cur + m - 1) % n or n
        if cur <= 1:
            break
        print(cur, end='')


if __name__ == '__main__':
    main()
