
def moveList(board, position, move, color):
    
    column, row = int(position[:1])-int(move[:1]), int(position[1:])-int(move[1:])





    # for x in range(int(position[:1])-1, 0, -1):
    #     new_position = f'{x}{position[1:]}'
    #     if '  ' != board[new_position]:
    #         if color != board[new_position][:1]:
    #             listMoves.append(new_position)
    #         break
    #     listMoves.append(new_position)

    # for x in range(int(position[:1])+1, 9):
    #     new_position = f'{x}{position[1:]}'
    #     if '  ' != board[new_position]:
    #         if color != board[new_position][:1]:
    #             listMoves.append(new_position)
    #         break
    #     listMoves.append(new_position)

    # for x in range(int(position[1:])-1, 0, -1):
    #     new_position = f'{position[:1]}{x}'
    #     if '  ' != board[new_position]:
    #         if color != board[new_position][:1]:
    #             listMoves.append(new_position)
    #         break
    #     listMoves.append(new_position)

    # for x in range(int(position[1:])+1, 9):
    #     new_position = f'{position[:1]}{x}'
    #     if '  ' != board[new_position]:
    #         if color != board[new_position][:1]:
    #             listMoves.append(new_position)
    #         break
    #     listMoves.append(new_position)

    return False

print(moveList(board={
    '18': 'bW', '28': 'Sb', '38': 'bG', '48': 'bH', '58': 'bK', '68': 'bG', '78': 'bS', '88': 'bW', 
    '17': 'bP', '27': 'bP', '37': 'bP', '47': 'bP', '57': 'bP', '67': 'bP', '77': 'bP', '87': 'bP',
    '16': '  ', '26': '  ', '36': '  ', '46': '  ', '56': '  ', '66': '  ', '76': '  ', '86': '  ',
    '15': '  ', '25': '  ', '35': '  ', '45': '  ', '55': '  ', '65': '  ', '75': '  ', '85': '  ',
    '14': '  ', '24': '  ', '34': '  ', '44': '  ', '54': '  ', '64': '  ', '74': '  ', '84': '  ',
    '13': '  ', '23': '  ', '33': '  ', '43': '  ', '53': '  ', '63': '  ', '73': '  ', '83': '  ',
    '12': '  ', '22': 'wP', '32': 'wP', '42': 'wP', '52': 'wP', '62': 'wP', '72': 'wP', '82': 'wP',
    '11': 'wW', '21': 'wS', '31': 'wG', '41': 'wH', '51': 'wK', '61': 'wG', '71': 'wS', '81': 'wW',
},position='11' ,color='w', move='15'))