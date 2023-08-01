matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
row_index = None
column_index = None
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_index = i
            column_index = j
row_moves = abs(row_index - 2) 
column_moves = abs(column_index - 2)  

minimum_moves = row_moves + column_moves
print(minimum_moves)
