def maximumWealth(accounts):

    max_value = 0

    for i in range (len(accounts)):
        total = 0
        for j in range (len(accounts[i])):
            total += accounts[i][j]
            print(total)
        if total > max_value:
            max_value = total

    print(max_value)
    return max_value


accounts =[[1,5],[7,3],[3,5]]

maximumWealth(accounts)

# print(len(accounts[0]))
