def removeIslands(matrix):
    # Write your code here.
    matrix = turn_to_matrix(matrix, 1, 2)
    for i in range(len(matrix)):
        print(matrix[i])   
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            elif matrix[i][j] == 2:
                matrix[i][j] = 1
    return matrix

def turn_to_matrix(matrix, initial_val, end_val):
    beginning = 0
    end_x = len(matrix) - 1
    end_y = len(matrix[0]) - 1
    edges_x = [beginning, end_x]
    edges_y = [beginning, end_y]
    print("ends: ", edges_x, edges_y)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in edges_x or  j in edges_y:
            # if matrix[i][j] == initial_val:
                # search all other 1s and turn them to 2
                depth_first_search(matrix, i, j, initial_val, end_val)
    return matrix

def depth_first_search(matrix, i, j, initial_val, end_val):
    # exit scenario
    # if i == 1 and j == 5:
    #     print("Here: ", i, j, matrix[i][j])
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return
    if matrix[i][j] != initial_val:
        return
    matrix[i][j] = end_val
    if j + 1 < len(matrix[0]):
        depth_first_search(matrix, i, j+1, initial_val, end_val)
    if j - 1 >= 0:
        depth_first_search(matrix, i, j-1, initial_val, end_val)
    if i + 1 < len(matrix):
        depth_first_search(matrix, i+1, j, initial_val, end_val)
    if i - 1 >= 0 :
        depth_first_search(matrix, i-1, j, initial_val, end_val)
    return
    
