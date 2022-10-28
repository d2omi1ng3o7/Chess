
def moveList(board, position, color, attacked_fields):

    listMoves = []
    to_del = []

    listMoves.append(f'{int(position[:1])}{int(position[1:])+1}')
    listMoves.append(f'{int(position[:1])+1}{int(position[1:])+1}')
    listMoves.append(f'{int(position[:1])+1}{int(position[1:])}')
    listMoves.append(f'{int(position[:1])+1}{int(position[1:])-1}')
    listMoves.append(f'{int(position[:1])}{int(position[1:])-1}')
    listMoves.append(f'{int(position[:1])-1}{int(position[1:])-1}')
    listMoves.append(f'{int(position[:1])-1}{int(position[1:])}')
    listMoves.append(f'{int(position[:1])-1}{int(position[1:])+1}')

    for x in listMoves:
        if int(x[:1]) >= 1 and int(x[1:]) <= 8:
            if (color == board[x][:1]) or (x in attacked_fields):
                to_del.append(x)
        else:
            to_del.append(x)

    for x in to_del:         
        listMoves.remove(x)

    return listMoves