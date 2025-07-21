matrix = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6],
]

row = len(matrix)
column = len(matrix[0])

top = 0
bottom = row - 1
left = 0
right = column - 1

while top <= bottom and left <= right:
    for i in range(left, right + 1 ):
        print(matrix[top][i], end = " ")
    top = top + 1

    for i in range(top, bottom + 1 ):
        print(matrix[i][right], end = " ")
    right = right - 1
    if(top<=bottom):
        for i in range(right, left-1, -1):
            print(matrix[bottom][i], end = " ")
        bottom = bottom - 1
    if(left<=right):
        for i in range(bottom, top-1, -1):
            print(matrix[i][left], end = " ")
        left = left + 1