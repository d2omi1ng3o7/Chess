from .constants import CHESS_BOARD


def moveList(board, position, color, lastMove='bP3735'):

    listWithMoves = []

    if board[f'{position[:1]}{int(position[1:])+1}'] == '  ' and color == 'w':
        listWithMoves.append(f'{position[:1]}{int(position[1:])+1}')
        if board[f'{position[:1]}{int(position[1:])+2}'] == '  ':    
            if position[1:] == '2':
                listWithMoves.append(f'{position[:1]}{int(position[1:])+2}')

    try:
        if board[f'{int(position[:1])+1}{int(position[1:])+1}'][:1] == 'b' and color == 'w':
            listWithMoves.append(f'{int(position[:1])+1}{int(position[1:])+1}')
    except:
        pass

    try:
        if board[f'{int(position[:1])-1}{int(position[1:])+1}'][:1] == 'b' and color == 'w':
                listWithMoves.append(f'{int(position[:1])-1}{int(position[1:])+1}')
    except:
        pass



        # if position[1:] == '5' and color == 'w' and lastMove[:2] == 'bP':
        #     if (lastMove[2:3] == f'{int(position[1:]+1)}' or lastMove[2:3] == f'{int(position[1:]+1)}')
        #         listWithMoves.append(f'{int(position[:1])+1}{int(position[1:])+1}')

    if board[f'{position[:1]}{int(position[1:])-1}'] == '  ' and color == 'b':
        listWithMoves.append(f'{position[:1]}{int(position[1:])-1}')
        if board[f'{position[:1]}{int(position[1:])-2}'] == '  ':    
            if position[1:] == '7':
                listWithMoves.append(f'{position[:1]}{int(position[1:])-2}')

    # if board[f'{int(position[:1])+1}{int(position[1:])-1}'][:1] == 'b' and color == 'b':
    #         listWithMoves.append(f'{int(position[:1])+1}{int(position[1:])-1}')
    # if board[f'{int(position[:1])-1}{int(position[1:])-1}'][:1] == 'b' and color == 'b':
    #     listWithMoves.append(f'{int(position[:1])-1}{int(position[1:])-1}')

    return listWithMoves