#!/usr/bin/env python
import sys


def solve(data):
    N, M, K = map(int, data.pop(0).split())
    p = int(data.pop(0))
    tn = [map(int, data.pop(0).split()) for i in xrange(p)]
    q = int(data.pop(0))
    nm = [map(int, data.pop(0).split()) for i in xrange(q)]
    r = int(data.pop(0))
    tm = [map(int, data.pop(0).split()) for i in xrange(r)]

    c = [(t, n, m) for t in range(1, N + 1)
                   for n in range(1, M + 1)
                   for m in range(1, K + 1)]
    g = filter(lambda (t, n, m): not ([t, n] in tn or [n, t] in tn or
                                      [t, m] in tm or [m, t] in tm or
                                      [n, m] in nm or [m, n] in nm), c)
    return len(g)


def main():
    data = sys.stdin.readlines()
    result = solve(data)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
