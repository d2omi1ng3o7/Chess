
def moveList(board, position, color):

    listMoves = []
    moves = (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)

    for move in moves:
        counter = 0
        while True:
            newPosition = f'{int(position[:1]) + move[0] + counter * move[0]}{int(position[1:]) + move[1] + counter * move[1]}'
            if int(newPosition[:1]) < 1 or int(newPosition[:1]) > 8 or int(newPosition[1:]) < 1 or int(newPosition[1:]) > 8: break
            if board[newPosition] != '  ':
                if color != board[newPosition][:1]:
                    listMoves.append(newPosition)
                    break
                else: break
            else: 
                listMoves.append(newPosition)
                counter += 1

    return listMoves