from constants import CHESS_BOARD

# generujesz listę ruchem i potem sprawdzasz czy użytkownik podał jakiś ruch z tej listy

class Rook:
    def __init__(self):
        self.listWithMoves = []
        self.moveAbovePieces = False
    

    def moveList(self, position='45'): # Do poprawy: dodaj możliwość wybrania dowolnej pozycji, połącz w jedno te same pętle linie i kolumny

        for x in range(int(position[:1])-1, 1, -1):
            new_position = f'{x}5'
            if not(self.moveAbovePieces) and '  ' != CHESS_BOARD[new_position]:
                break
            self.listWithMoves.append(new_position)

        for x in range(int(position[:1])+1, 9):
            new_position = f'{x}5'
            if not(self.moveAbovePieces) and '  ' != CHESS_BOARD[new_position]:
                break
            self.listWithMoves.append(new_position)

        for x in range(int(position[1:])-1, 1, -1):
            new_position = f'4{x}'
            if not(self.moveAbovePieces) and '  ' != CHESS_BOARD[new_position]:
                break
            self.listWithMoves.append(new_position)

        for x in range(int(position[1:])+1, 9):
            new_position = f'4{x}'
            if not(self.moveAbovePieces) and '  ' != CHESS_BOARD[new_position]:
                break
            self.listWithMoves.append(new_position)

        return self.listWithMoves

obj = Rook()

obj.moveList()
print(obj.listWithMoves)