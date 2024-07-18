def largestLocal(grid):

    maxLocal = []
    all_values = [] 
    max_value = []

    for i in range (len(grid) - 2):
        for j in range (len(grid[i]) - 2):

            all_values.append(grid[i][j])
            all_values.append(grid[i][j + 1])
            all_values.append(grid[i][j + 2])

            all_values.append(grid[i + 1][j])
            all_values.append(grid[i + 1][j + 1])
            all_values.append(grid[i + 1][j + 2])

            all_values.append(grid[i + 2][j])
            all_values.append(grid[i + 2][j + 1])
            all_values.append(grid[i + 2][j + 2])

            max_value.append(max(all_values))

            all_values = []

        maxLocal.insert(i, max_value)
        max_value = []
       

    return(maxLocal)

grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
largestLocal(grid)
