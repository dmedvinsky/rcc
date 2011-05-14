#!/usr/bin/env python
import sys
from math import factorial


def solve(data):
    def get_task(_):
        L, m = map(int, data.pop(0).split())
        S1 = data.pop(0).strip()
        S2 = data.pop(0).strip()
        return (L, m, S1, S2)
    t = int(data.pop(0))
    tasks = map(get_task, xrange(t))
    results = map(solve_one, tasks)
    return '\n'.join(map(str, results))


def solve_one((L, m, S1, S2)):
    def f(diff):
        if diff == 0:
            return 2
        elif diff > 0:
            n = 21
            k = diff
            return factorial(n + k - 1) / (factorial(k) * factorial(n - 1)) * 2
        else:
            c = 0
            for l in range(1, len(S1) + 1):
                if S2.startswith(S1[-l:]) and len(S1) + len(S2) - l == L:
                    c += 1
            for l in range(1, len(S2) + 1):
                if S1.startswith(S2[-l:]) and len(S1) + len(S2) - l == L:
                    c += 1
            return c
    return f(L - (len(S1) + len(S2))) % m


def main():
    data = sys.stdin.readlines()
    result = solve(data)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
