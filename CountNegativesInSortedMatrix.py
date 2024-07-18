def countNegatives(grid):

    total_negatives = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < 0:
                total_negatives += 1

    print(total_negatives)

    return total_negatives
