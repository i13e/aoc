from itertools import product

from aocd import data

def part_1(s: str):
    mat = [line.strip() for line in s.splitlines()]
    R = range(len(mat))
    C = range(len(mat[0]))

    res = 0
    for sr, sc in product(R, C):
        for dr, dc in product(range(-1, 2), repeat=2):
            r, c = sr, sc
            for s in "XMAS": 
                if r not in R or c not in C or mat[r][c] != s:
                    break
                r, c = r + dr, c + dc
            else:
                res += 1


    return res



def part_2(s: str):
    rows = [line.strip() for line in s.splitlines()]
    m = len(rows)
    n = len(rows[0])

    def check(r, c):
        if rows[r][c] != 'A':
            return False
        ul = rows[r-1][c-1]
        ur = rows[r-1][c+1]
        dl = rows[r+1][c-1]
        dr = rows[r+1][c+1]
        return sorted([ul, ur, dl, dr]) == ['M', 'M', 'S', 'S'] and ul != dr

    return sum(check(r, c) for r in range(1, m-1) for c in range(1, n-1))
