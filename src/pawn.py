
def moveList(board, position, color, lastMove='bP3735'):

    listMoves = []

    if board[f'{position[:1]}{int(position[1:]) + (1 if color == "w" else -1)}'] == '  ':
        listMoves.append(f'{position[:1]}{int(position[1:]) + (1 if color == "w" else -1)}')
    
    if position[1:] == ('2' if color == "w" else '7') and board[f'{position[:1]}{int(position[1:]) + (2 if color == "w" else -2)}'] == '  ':
        listMoves.append(f'{position[:1]}{int(position[1:]) + (2 if color == "w" else -2)}')
            
    try:
        if board[f'{int(position[:1])+1}{int(position[1:]) + (1 if color == "w" else -1)}'][:1] == ('b' if color == "w" else 'w'):
            listMoves.append(f'{int(position[:1])+1}{int(position[1:])+1}')
    except: pass
    
    try:
        if board[f'{int(position[:1])-1}{int(position[1:]) + (1 if color == "w" else -1)}'][:1] == ('b' if color == "w" else 'w'):
                listMoves.append(f'{int(position[:1])-1}{int(position[1:])+1}')
    except: pass

    return listMoves