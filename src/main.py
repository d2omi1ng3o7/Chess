import os
from .king import moveList as king
from .queen import moveList as queen
from .rook import moveList as rook
from .bishop import moveList as bishop
from .knight import moveList as knight
from .pawn import moveList as pawn



class ChessGame():
    def __init__(self, board):
        self.board = board
        self.whose_move = True # True - white False - black
        self.isCheck = False
        self.isCheckmate = False
        self.isDraw = False
        self.whoWin = ('white', 'black', '')
        self.lastMove = ''


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

    def getMoves(self): # dodać dowanie pozycji w tych wszystkich funkcjach z ruchami
        listAllMoves = []
        attachedFields = []

        for column in range(1, 9):
            for row in range(1, 9):
                position = f'{column}{row}'
                color = self.board[position][:1]
                piece = self.board[position][1:]

                if self.board[position] == '  ':
                    continue
                
                match piece:
                    case 'K':
                        if self.whose_move:
                            c = 'w'
                        else: 
                            c = 'b'
                        if color == c:
                            kingPosition = position
                        else:
                            listMoves = king(self.board, position, color, [])
                    case 'Q': listMoves = queen(self.board, position, color)
                    case 'R': listMoves = rook(self.board, position, color)
                    case 'B': listMoves = bishop(self.board, position, color)
                    case 'S': listMoves = knight(self.board, position, color)
                    case 'P': listMoves = pawn(self.board, position, color, self.lastMove)
                    case other: listMoves = []

                if self.whose_move:
                    if color == 'w':
                        for x in listMoves:
                            listAllMoves.append(f'{position}{x}')
                    else:
                        for x in listMoves:
                            attachedFields.append(x)
                else:
                    if color == 'b':
                        for x in listMoves:
                            listAllMoves.append(f'{position}{x}')
                    else:
                        for x in listMoves:
                            attachedFields.append(x)
        
        listMoves = king(self.board, kingPosition, color, attachedFields)
        for x in listMoves:
            listAllMoves.append(f'{position}{x}')

        if kingPosition in attachedFields:
            print('sdfsdfsdfsdf')
            for x in listAllMoves:
                if kingPosition != x[:2]:
                    listAllMoves.remove(x)

        return listAllMoves

    def move(self, listAllMoves):
        move = input()
        color = self.board[move[:2]][:1]

        if self.whose_move:
            if color != 'w': return
        else:
            if color != 'b': return
        
        if not self.isCheck:
            match self.board[move[:2]][1:]:
                case 'K': listMoves = king(board=self.board, position=move[:2], color=color, attacked_fields=[])
                case 'Q': listMoves = queen(board=self.board, position=move[:2], color=color)
                case 'R': listMoves = rook(board=self.board, position=move[:2], color=color)
                case 'B': listMoves = bishop(board=self.board, position=move[:2], color=color)
                case 'S': listMoves = knight(board=self.board, position=move[:2], color=color)
                case 'P': listMoves = pawn(board=self.board, position=move[:2], color=color, lastMove='')
                case other: listMoves = []
        else:
            listMoves = king(board=self.board, position=move[:2], color=color, attacked_fields=[])
            if listMoves == []:
                pass

        if move[2:4] in listMoves:
            self.board[move[2:4]] = self.board[move[:2]]
            self.board[move[:2]] = '  '
        else: return

        if self.whose_move: self.whose_move = False 
        else: self.whose_move = True