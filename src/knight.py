from constants import CHESS_BOARD


class Knight:
    def __init__(self):
        pass

    def moveList(self, position='25', color='w'):

        listWithMoves = []
        to_del = []

        listWithMoves.append(f'{int(position[:1])+1}{int(position[1:])+2}')
        listWithMoves.append(f'{int(position[:1])+2}{int(position[1:])+1}')
        listWithMoves.append(f'{int(position[:1])+2}{int(position[1:])-1}')
        listWithMoves.append(f'{int(position[:1])+1}{int(position[1:])-2}')
        listWithMoves.append(f'{int(position[:1])-1}{int(position[1:])-2}')
        listWithMoves.append(f'{int(position[:1])-2}{int(position[1:])-1}')
        listWithMoves.append(f'{int(position[:1])-2}{int(position[1:])+1}')
        listWithMoves.append(f'{int(position[:1])-1}{int(position[1:])+2}')

        for x in listWithMoves:
            if int(x[:1]) >= 1 and int(x[1:]) <= 8:
                if color == CHESS_BOARD[x][:1]:
                    to_del.append(x)
            else:
                to_del.append(x)

        for x in to_del:         
            listWithMoves.remove(x)
        
        return listWithMoves