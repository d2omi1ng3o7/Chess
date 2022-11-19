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

Ruch {'białych' if self.whoseMove else 'czarnych'}.
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

    def convert(self, listMove, list):
        for move in listMove:
            list.append(move)

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
                                self.convert(listMoves, listAllMoves)
                            else:
                                self.convert(listMoves, attachedFields)
                        else:
                            if color == 'b':
                                self.convert(listMoves, listAllMoves)
                            else:
                                self.convert(listMoves, attachedFields)

                    case 'R': 
                        listMoves = rook(self.board, position, color)
                        if self.whoseMove:
                            if color == 'w':
                                self.convert(listMoves, listAllMoves)
                            else:
                                self.convert(listMoves, attachedFields)
                        else:
                            if color == 'b':
                                self.convert(listMoves, listAllMoves)
                            else:
                                self.convert(listMoves, attachedFields)
                    case 'B': 
                        listMoves = bishop(self.board, position, color)
                        if self.whoseMove:
                            if color == 'w':
                                self.convert(listMoves, listAllMoves)
                            else:
                                self.convert(listMoves, attachedFields)
                        else:
                            if color == 'b':
                                self.convert(listMoves, listAllMoves)
                            else:
                                self.convert(listMoves, attachedFields)
                    case 'S': 
                        listMoves = knight(self.board, position, color)
                        if self.whoseMove:
                            if color == 'w':
                                self.convert(listMoves, listAllMoves)
                            else:
                                self.convert(listMoves, attachedFields)
                        else:
                            if color == 'b':
                                self.convert(listMoves, listAllMoves)
                            else:
                                self.convert(listMoves, attachedFields)
                    case 'P':
                        continue # popraw pawn.py by było osobno szukanie atakowanych pól i możliwego ruszania się i potem uwzględnij to tu

        self.convert(king(self.board, (self.blackKingPosition if self.whoseMove else self.whiteKingPosition), ('b' if self.whoseMove else 'w')), attachedFields)
        self.convert(king(self.board, (self.whiteKingPosition if self.whoseMove else self.blackKingPosition), ('w' if self.whoseMove else 'b'), attachedFields), listAllMoves)

        for i in attachedFields:
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
        if self.isCheckmate:
            return f'Wygrał {self.whose_move}'

        move = input()
        color = self.board[move[:2]][:1]

        if self.whoseMove:
            if color != 'w': return
        else:
            if color != 'b': return
        
        for x in listAllMoves:
            if move in x:
                self.board[move[2:4]] = self.board[move[:2]]
                self.board[move[:2]] = '  '
            else:
                return

        if self.whoseMove:
            self.whoseMove = False 
        else:
            self.whoseMove = True