def isSolved(board):
    # 0 is empty, 1 is X, 2 is an O
    #print board[0], board[1], board[2]
    #print board[0][2]
    sameij = []
    difij = []
    zeros = 0
    incomplete = True   # if incomplete = true, return -1
    draw = True         # if draw = true, return 0
    for i in range(3):
        countj = []
        for j in range(3):
            # print board[i][j]
            if board[i][j] == 0: zeros += 1
            countj.append(board[i][j])
            if i == j:
                sameij.append(board[i][j])
            if i + j ==2:
                difij.append(board[i][j])
        if (countj[0] == countj[1] == countj[2]):
            if (countj[0] + countj[1] + countj[2] == 3):
                incomplete = False
                draw = False
                return  1
            if (countj[0] + countj[1] + countj[2] == 6):
                incomplete = False
                draw = False
                return  2
          #  else:
           #     return "Not sure yet"
    if (sameij[0] == sameij[1] == sameij[2]):
        if (sameij[0] + sameij[1] + sameij[2] == 3):
            incomplete = False
            draw = False
            return  1
        if (sameij[0] + sameij[1] + sameij[2] == 6):
            incomplete = False
            draw = False
            return  2
        #else:
         #   return "Not sure yet"
    if (difij[0] == difij[1] == difij[2]):
        if (difij[0] + difij[1] + difij[2] == 3):
            incomplete = False
            draw = False
            return  1
        if (difij[0] + difij[1] + difij[2] == 6):
            incomplete = False
            draw = False
            return  2
        #else:
         #   return "Not sure yet"

    for j in range(3):
        countj = []
        for i in range(3):
            # print board[i][j]
            countj.append(board[i][j])
        if (countj[0] == countj[1] == countj[2]):
            if (countj[0] + countj[1] + countj[2] == 3):
                incomplete = False
                draw = False
                return  1
            if (countj[0] + countj[1] + countj[2] == 6):
                incomplete = False
                draw = False
                return  2
            #else:
             #   return "...Not sure yet"
    if zeros > 0:
        return -1
    if draw:
        return 0



    # Return -1 if not solved, 1 if X won, 2 if O won, 0 if draw


board1 = [[1,2,1],[1,2,0],[2,1,0]]
board = [[2,0,2],[2,1,1],[1,2,1]]
print isSolved(board)



