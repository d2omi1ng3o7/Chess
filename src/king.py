from .constants import CHESS_BOARD



def moveList(position='53', color='w', attacked_fields=['44']):

    listWithMoves = []
    to_del = []

    listWithMoves.append(f'{int(position[:1])}{int(position[1:])+1}')
    listWithMoves.append(f'{int(position[:1])+1}{int(position[1:])+1}')
    listWithMoves.append(f'{int(position[:1])+1}{int(position[1:])}')
    listWithMoves.append(f'{int(position[:1])+1}{int(position[1:])-1}')
    listWithMoves.append(f'{int(position[:1])}{int(position[1:])-1}')
    listWithMoves.append(f'{int(position[:1])-1}{int(position[1:])-1}')
    listWithMoves.append(f'{int(position[:1])-1}{int(position[1:])}')
    listWithMoves.append(f'{int(position[:1])-1}{int(position[1:])+1}')

    for x in listWithMoves:
        if int(x[:1]) >= 1 and int(x[1:]) <= 8:
            if (color == CHESS_BOARD[x][:1]) or (x in attacked_fields):
                to_del.append(x)
        else:
            to_del.append(x)

    for x in to_del:         
        listWithMoves.remove(x)

    return listWithMoves