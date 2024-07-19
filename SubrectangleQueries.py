class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                print("i e j: ", i , j )
                self.rectangle[i][j] = newValue
        return

    def getValue(self, row, col):
        return self.rectangle[row][col]


obj = SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]])
print(obj.getValue(0, 0))
obj.updateSubrectangle(0, 0, 2, 2, 100)
print(obj.getValue(0, 0))
print(obj.getValue(2, 2))
obj.updateSubrectangle(1, 1, 2, 2, 20)
print(obj.getValue(2,2))
