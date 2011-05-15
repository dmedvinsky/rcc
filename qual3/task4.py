#!/usr/bin/env python
import sys
from itertools import combinations

def solve(data):
    n, P = map(int, data.pop(0).strip().split())
    ms = map(int, data.pop(0).strip().split())

    def pack_special(ms):
        for l in range(1, len(ms) + 1):
            ps = combinations(ms, l)
            for p in ps:
                if sum(p) == 1000:
                    return p

    specials = []
    while len(ms):
        p = pack_special(ms)
        if p is not None:
            specials.append(p)
            map(lambda m: ms.remove(m), p)
        else:
            break

    return P * len(specials) + sum(ms)


def main():
    data = sys.stdin.readlines()
    result = solve(data)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
