
def moveList(board, position, color):

    listMoves = []

    for x in range(int(position[:1])-1, 0, -1):
        new_position = f'{x}{position[1:]}'
        if '  ' != board[new_position]:
            if color != board[new_position][:1]:
                listMoves.append(new_position)
            break
        listMoves.append(new_position)

    for x in range(int(position[:1])+1, 9):
        new_position = f'{x}{position[1:]}'
        if '  ' != board[new_position]:
            if color != board[new_position][:1]:
                listMoves.append(new_position)
            break
        listMoves.append(new_position)

    for x in range(int(position[1:])-1, 0, -1):
        new_position = f'{position[:1]}{x}'
        if '  ' != board[new_position]:
            if color != board[new_position][:1]:
                listMoves.append(new_position)
            break
        listMoves.append(new_position)

    for x in range(int(position[1:])+1, 9):
        new_position = f'{position[:1]}{x}'
        if '  ' != board[new_position]:
            if color != board[new_position][:1]:
                listMoves.append(new_position)
            break
        listMoves.append(new_position)

    for x in range(1, max(8-int(position[:1]), int(position[1:])-1)+1):
        new_position = f'{str(int(position[:1])-x)}{str(int(position[1:])+x)}'
        if '  ' != board[new_position]:
            if color != board[new_position][:1]:
                listMoves.append(new_position)
            break
        listMoves.append(new_position)

    for x in range(1, max(8-int(position[:1]), 8-int(position[1:]))+1):
        new_position = f'{str(int(position[:1])+x)}{str(int(position[1:])+x)}'
        if '  ' != board[new_position]:
            if color != board[new_position][:1]:
                listMoves.append(new_position)
            break
        listMoves.append(new_position)

    for x in range(1, max(int(position[:1])-1, 8-int(position[1:]))+1):
        new_position = f'{str(int(position[:1])+x)}{str(int(position[1:])-x)}'
        if '  ' != board[new_position]:
            if color != board[new_position][:1]:
                listMoves.append(new_position)
            break
        listMoves.append(new_position)

    for x in range(1, max(int(position[:1])-1, int(position[1:])-1)+1):
        new_position = f'{str(int(position[:1])-x)}{str(int(position[1:])-x)}'
        if '  ' != board[new_position]:
            if color != board[new_position][:1]:
                listMoves.append(new_position)
            break
        listMoves.append(new_position)

    return listMoves