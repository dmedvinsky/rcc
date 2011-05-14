#!/usr/bin/env python
import sys
import math


def solve(data):
    _, r = map(int, data.pop(0).split())
    vals = map(int, data.pop(0).split())

    r2 = r * r
    pir2 = math.pi * r2
    total = sum(vals)
    alphas = map(lambda a: 360 / float(total) * a, vals)
    results = map(lambda a: pir2 / 360 * a, alphas)
    return '\n'.join(map(str, results))


def main():
    data = sys.stdin.readlines()
    result = solve(data)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
