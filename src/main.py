import os
from .king import moveList as king
from .queen import moveList as queen
from .rook import moveList as rook
from .bishop import moveList as bishop
from .knight import moveList as knight
from .pawn import moveList as pawn
from .check import check


class ChessGame():
    def __init__(self, board):
        self.board = board
        self.whoseMove = True  # True - white False - black
        self.isCheck = False
        self.isCheckmate = False
        self.lastMove = ''
        self.whiteKingPosition = '51'
        self.blackKingPosition = '58'

    def printChessBoard(self):

        print(
f"""

X - kolumna Y - wiersz (Podawać tylko liczby!)
Podaj kordynaty figury którą chcesz ruszyć,
a następne bez odstępu kordynaty pola na którze chcesz ruszyć.

                            XYXY

Ruch {'białych' if self.whose_move else 'czarnych'}.
""")

        print('---------------------------------------------------------')
        counter = 1
        for i in self.board:
            print(f'|  {self.board[i]}  ', end='', sep='')
            if counter == 8:
                print('|', end='')
                print('\n', '---------------------------------------------------------', sep='')
                counter = 1
            else: counter += 1
        print()
    
    def clearScreen(self):
        os.system('cls') if os.name == 'nt' else os.system('clear')

    def getMoves(self):
        listAllMoves = []
        attachedFields = []

        for column in range(1, 9):
            for row in range(1, 9):
                position = f'{column}{row}'
                color = self.board[position][:1]
                piece = self.board[position][1:]


                match piece:
                    case ' ':
                        continue
                    case 'K':
                        continue
                    case 'Q': 
                        listMoves = queen(self.board, position, color)
                        if self.whoseMove:
                            if color == 'w':
                                listAllMoves.append(listMoves)
                            else:
                                attachedFields.append(listMoves)
                        else:
                            if color == 'b':
                                listAllMoves.append(listMoves)
                            else:
                                attachedFields.append(listMoves)

                    case 'R': 
                        listMoves = rook(self.board, position, color)
                        if self.whoseMove:
                            if color == 'w':
                                listAllMoves.append(listMoves)
                            else:
                                attachedFields.append(listMoves)
                        else:
                            if color == 'b':
                                listAllMoves.append(listMoves)
                            else:
                                attachedFields.append(listMoves)
                    case 'B': 
                        listMoves = bishop(self.board, position, color)
                        if self.whoseMove:
                            if color == 'w':
                                listAllMoves.append(listMoves)
                            else:
                                attachedFields.append(listMoves)
                        else:
                            if color == 'b':
                                listAllMoves.append(listMoves)
                            else:
                                attachedFields.append(listMoves)
                    case 'S': 
                        listMoves = knight(self.board, position, color)
                        if self.whoseMove:
                            if color == 'w':
                                listAllMoves.append(listMoves)
                            else:
                                attachedFields.append(listMoves)
                        else:
                            if color == 'b':
                                listAllMoves.append(listMoves)
                            else:
                                attachedFields.append(listMoves)
                    case 'P':
                        continue # popraw pawn.py by było osobno szukanie atakowanych pól i możliwego ruszania się i potem uwzględnij to tu

        for x in attachedFields:
            for i in x:
                if i[2:] == (self.whiteKingPosition if self.whoseMove else self.blackKingPosition):
                    self.isCheck = True

        if self.isCheck:
            listAllMoves = check(listAllMoves, attachedFields)

        bool = True       # czy mat
        for x in listAllMoves:
            if x != []:
                bool = False

        if bool:
            self.isCheckmate = True
        

        self.isCheck = False

        return listAllMoves

    def move(self, listAllMoves):
        move = input()
        color = self.board[move[:2]][:1]

        if self.whose_move:
            if color != 'w': return
        else:
            if color != 'b': return
        
        for x in listAllMoves:
            if move in x:
                self.board[move[2:4]] = self.board[move[:2]]
                self.board[move[:2]] = '  '
            else:
                return

        if self.whose_move:
            self.whose_move = False 
        else:
            self.whose_move = True