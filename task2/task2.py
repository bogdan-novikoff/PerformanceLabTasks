import sys


def main():
    file1, file2 = sys.argv[1:]

    with open(file1, 'r') as file:
        center, radius = file.readlines()
        x0, y0 = map(float, center.split())
        radius = float(radius)

    with open(file2, 'r') as file:
        lines = file.readlines()
        dots = list(
            zip(map(lambda line: float(line.split()[0]), lines), map(lambda line: float(line.split()[1]), lines))
        )

    for x, y in dots:
        r = ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5
        print(0 if r == radius else 1 if r < radius else 2)


if __name__ == '__main__':
    main()
