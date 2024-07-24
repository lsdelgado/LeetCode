def restoreMatrix(rowSum, colSum):

    rows = len(rowSum)
    cols = len(colSum)

    ans = [[0] * cols for _ in range (rows)]

    for r in range(rows):
        ans[r][0] = rowSum[r]
        print("for 1: ", ans)

    for c in range(cols):
        total_cols = 0
        for r in range(rows):
            total_cols += ans[r][c]

        print("ans antes do while ", ans)

        r = 0

        while total_cols > colSum[c]:
            diff = total_cols - colSum[c]
            max_value = min(ans[r][c], diff)
            ans[r][c] -= max_value
            ans[r][c+1] += max_value
            total_cols -= max_value
            r += 1
    
    print(ans)
    return ans


rowSum = [5,7,10]
colSum = [8,6,8]
restoreMatrix(rowSum, colSum)
