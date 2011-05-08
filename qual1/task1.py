#!/usr/bin/env python
import sys


def solve(data):
    parts = map(lambda s: s.split(')'), data.split('('))
    return reduce(lambda r, p: r + (p[0][::-1] + p[1] if len(p) > 1 else p[0]),
                  parts, '')


def main():
    data = sys.stdin.readlines()
    data = ''.join(data)
    result = solve(data)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
