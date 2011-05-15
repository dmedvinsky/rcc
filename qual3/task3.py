#!/usr/bin/env python
import sys


def solve(data):
    def get_window(l):
        parts = l.strip().split()
        o = map(int, parts[0].split(':'))
        c = map(int, parts[1].split(':'))
        return o[0] * 60 + o[1], c[0] * 60 + c[1], int(parts[2])
    in_h, in_m = map(int, data.pop(0).split(':'))
    n = int(data.pop(0))
    windows = map(get_window, data)

    pad = lambda v: ('%d' if v >= 10 else '0%d') % v
    time = in_h * 60 + in_m
    for o, c, d in windows:
        enter = max(o, time)
        leave = enter + d
        if leave > c:
            time = 23 * 60
            break
        else:
            time = leave
    h, m = divmod(time, 60)
    return 'No' if h >= 23 else '\n'.join(['Yes', '%s:%s' % (pad(h), pad(m))])


def main():
    data = sys.stdin.readlines()
    result = solve(data)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
