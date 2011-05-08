#!/usr/bin/env python
import sys
from math import ceil


def solve(data):
    data.pop(0)
    calls = map(int, data.pop().split())
    tarifs = map(lambda s: map(int, s.split()), data)

    def p((c, t, p)):
        return reduce(lambda s, T: s + (0 if T < t else p * ceil(T / float(t))),
                      calls, c * 100)

    results = map(p, tarifs)
    return results.index(min(results)) + 1


def main():
    data = sys.stdin.readlines()
    result = solve(data)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
