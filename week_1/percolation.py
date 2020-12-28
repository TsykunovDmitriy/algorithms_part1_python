import random
import argparse
import numpy as np
from weighted_quickunion import WeighedQuickUnion

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, default=8, help='width/height of grid')
    parser.add_argument('--p', type=int, default=0.6, help='probability if white cell')
    args = parser.parse_args()

    grid = []
    for i in range(args.N):
        row = []
        for j in range(args.N):
            item = 1 if random.uniform(0, 1) <= args.p else 0
            row.append(item)
        grid.append(row)
    print(np.matrix(grid))

    qu = WeighedQuickUnion(args.N*args.N + 2)
    for i in range(1, args.N + 1):
        qu.union(0, i)
        qu.union(args.N*args.N + 1, args.N*(args.N - 1) + i)

    if grid[0][0] == 1:
        if grid[1][0] == 1:
            qu.union(1, args.N + 1)
        if grid[0][1] == 1:
            qu.union(1, 2)

    if grid[0][args.N - 1] == 1:
        if grid[1][args.N - 1] == 1:
            qu.union(args.N, args.N + args.N)
        if grid[0][args.N - 2] == 1:
            qu.union(args.N, args.N - 1)

    if grid[args.N - 1][0] == 1:
        if grid[args.N - 2][0] == 1:
            qu.union(args.N*(args.N - 1) + 1, args.N*(args.N - 2) + 1)
        if grid[args.N - 1][1] == 1:
            qu.union(args.N*(args.N - 1) + 1, args.N*(args.N - 1) + 2)

    if grid[args.N - 1][args.N - 1] == 1:
        if grid[args.N - 2][args.N - 1] == 1:
            qu.union(args.N*args.N, args.N*(args.N - 1))
        if grid[args.N - 1][args.N - 2] == 1:
            qu.union(args.N*args.N, args.N*args.N - 1)

    for i in range(1, args.N - 1):
        for j in range(1, args.N - 1):
            if grid[i][j] == 1:
                if grid[i - 1][j] == 1:
                    qu.union(i*args.N +j + 1, (i - 1)*args.N +j + 1)
                if grid[i + 1][j] == 1:
                    qu.union(i*args.N +j + 1, (i + 1)*args.N +j + 1)
                if grid[i][j - 1] == 1:
                    qu.union(i*args.N +j + 1, i*args.N +(j - 1) + 1)
                if grid[i][j + 1] == 1:
                    qu.union(i*args.N +j + 1, i*args.N +(j + 1) + 1)

    print(qu.connected(0, args.N*args.N + 1))
            