def diagonalSum(mat):

    diagonals_sum = 0

    for i in range (len(mat)):
        diagonals_sum += mat[i][i]

    j = len(mat[i]) - 1
    center = len(mat)//2
    print("center", center)

    for i in range (len(mat)):

        print(i, j)

        if mat[i][j] == mat[i][i] and len(mat) % 2 > 0 and j == center:
            if mat[i][j] == mat[center][center]:
                j -= 1

        else:
            diagonals_sum += mat[i][j]
            print("aqui", mat[i][j])
            j -= 1

    print(diagonals_sum)

    return diagonals_sum

# mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]] # resultado 8
mat =[[4,6,7],[2,9,4],[5,5,5]] # resultado 30

diagonalSum(mat)

