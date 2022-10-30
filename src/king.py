
def moveList(board, position, color, attacked_fields):

    listMoves = []
    moves = (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)

    for move in moves:
        newPosition = f'{int(position[:1]) + move[0]}{int(position[1:]) + move[1]}'
        if int(newPosition[:1]) < 1 or int(newPosition[:1]) > 8 or int(newPosition[1:]) < 1 or int(newPosition[1:]) > 8: continue
        if board[newPosition] != '  ':
            if color != board[newPosition][:1] or newPosition not in attacked_fields:
                listMoves.append(newPosition)
                continue
            else: continue
        else: 
            listMoves.append(newPosition)

    return listMoves