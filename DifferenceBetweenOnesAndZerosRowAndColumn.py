def onesMinusZeros(grid):

    r = len(grid)
    c = len(grid[0])

    diff = [[0] * c for _ in range(r)]

    rows = [0] * r
    cols = [0] * c

    for i in range (r):
        for j in range (c):
            print("i e j: ", i, j)
            if grid[i][j] == 1:
                rows[i] += 1
                cols[j] += 1

                print(rows, cols)


    for i in range (r):
        for j in range (c):
            diff[i][j] = rows[i] + cols[j] - (r - rows[i]) - (c - cols[j])

    print("diff", diff)
    return diff 

grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]

onesMinusZeros(grid)
