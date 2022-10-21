from constants import CHESS_BOARD


class Pawn:
    def __init__(self):
        pass

    def moveList(self, position='22', color='w', lastMove='35'):

        listWithMoves = []

        
        listWithMoves.append(f'{position[:1]}{int(position[1:])+1}')
        if (position[1:] == '2' and color =='w') or (position[:1] == '2' and color=='w'):
            listWithMoves.append(f'{position[:1]}{int(position[1:])+2}')
       
        for x in range(int(position[:1])-1, 1, -1):
            new_position = f'{x}{position[1:]}'
            if '  ' != CHESS_BOARD[new_position]:
                if color != CHESS_BOARD[new_position][:1]:
                    listWithMoves.append(new_position)
                break
            listWithMoves.append(new_position)


        return listWithMoves

obj = Pawn()

print(obj.moveList())