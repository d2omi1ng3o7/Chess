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

        print(listWithMoves)
        for x in range(8):
            if int(listWithMoves[x][:1]) >= 1 and int(listWithMoves[x][1:]) <= 8:
                if color == CHESS_BOARD[listWithMoves[x]][:1]:
                    to_del.append(x)
            else:
                to_del.append(x)

        counter = 0
        for x in range(len(to_del)):
            listWithMoves.pop(to_del[x-counter])
            counter += 1
        
        return listWithMoves