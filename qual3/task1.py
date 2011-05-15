#!/usr/bin/env python
import sys
from math import sqrt, pow


def solve(data):
    n, d = map(int, data.pop(0).split())
    holes = map(lambda s: map(int, s.split()), data)

    fs = filter(lambda (_, __, t): bool(t), holes)
    zs = filter(lambda (_, __, t): not bool(t), holes)

    calc = lambda x1, y1, x2, y2: sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    ds = [calc(xf, xz, yf, yz) for xf, yf, _ in fs for xz, yz, _ in zs]
    return 'Yes' if d in ds else 'No'


def main():
    data = map(lambda s: s.strip(), sys.stdin.readlines())
    result = solve(data)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
