
def moveList(board, position, color):

    listMoves = []
    moves = (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, -1), (-1, 2)

    for move in moves:
        newPosition = f'{int(position[:1]) + move[0]}{int(position[1:]) + move[1]}'
        if int(newPosition[:1]) < 1 or int(newPosition[:1]) > 8 or int(newPosition[1:]) < 1 or int(newPosition[1:]) > 8: continue
        if board[newPosition] != '  ':
            if color != board[newPosition][:1]:
                listMoves.append(f'{position}{newPosition}')
                continue
            else: continue
        else: 
            listMoves.append(f'{position}{newPosition}')

    return listMoves