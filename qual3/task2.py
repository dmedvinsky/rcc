#!/usr/bin/env python
import sys


def solve(data):
    w, h = map(int, data.pop(0).split())
    squares = data

    border = 0
    for y in range(h):
        for x in range(w):
            if len(squares[y]) > x + 1 and squares[y][x] != squares[y][x + 1]:
                border += 1
            if len(squares) > y + 1 and squares[y][x] != squares[y + 1][x]:
                border += 1
    return border


def main():
    data = map(lambda s: s.strip(), sys.stdin.readlines())
    result = solve(data)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
