import numpy as np

def solution(rows, columns, queries=None):
    array = [[0] * columns for i in range(rows)]  
    
    count = 0
    for i in range(rows):
        for j in range(columns):
            count += 1
            array[i][j] = count
    
    minimum_value = []
    for index in range(len(queries)):
        x1, y1, x2, y2 = queries[index][0]-1, queries[index][1]-1, queries[index][2]-1, queries[index][3]-1
        
        up_next_array = []
        up_next_index = []
        for i in range(y1, y2):
            up_next_array.append(array[x1][i])
            up_next_index.append((x1, i+1))
            
        right_next_array = []
        right_next_index = []
        for i in range(x1, x2):
            right_next_array.append(array[i][y2])
            right_next_index.append((i+1, y2))
            
        down_next_array = []
        down_next_index = []
        for i in range(y1+1, y2+1):
            down_next_array.append(array[x2][i])
            down_next_index.append((x2, i-1))
        
        left_next_array = []
        left_next_index = []
        for i in range(x1+1, x2+1):
            left_next_array.append(array[i][y1])
            left_next_index.append((i-1, y1))
            
        down_next_array = list(reversed(down_next_array))
        down_next_index = list(reversed(down_next_index))
        left_next_array = list(reversed(left_next_array))
        left_next_index = list(reversed(left_next_index))

        rotate_array = up_next_array+right_next_array+down_next_array+left_next_array
        rotate_index = up_next_index+right_next_index+down_next_index+left_next_index
        
        for i in range(len(rotate_array)):
            x, y = rotate_index[i]
            array[x][y] = rotate_array[i]
            
        minimum_value.append(min(rotate_array))
    return minimum_value
    
    
queries = [[1, 1, 6, 6]]
solution(12, 6, queries)