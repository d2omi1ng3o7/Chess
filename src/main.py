from . import constants as const
import os
from .king import moveList as king
from .queen import moveList as queen
from .rook import moveList as rook
from .bishop import moveList as bishop
from .knight import moveList as knight
from .pawn import moveList as pawn



class Chess():
    def __init__(self):
        self.chess_board = const.CHESS_BOARD
        self.whose_move = True # True - white False - black
        self.isCheck = False
        self.isCheckmate = False
        self.isDraw = False
        self.whoWin = ('white', 'black', '')


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
        for i in self.chess_board:
            print(f'|  {self.chess_board[i]}  ', end='', sep='')
            if counter == 8:
                print('|', end='')
                print('\n', '---------------------------------------------------------', sep='')
                counter = 1
            else: counter += 1
        print()
    
    def clear_screen(self):
        os.system('cls') if os.name == 'nt' else os.system('clear')

    def move(self):
        move = input()
        color = self.chess_board[move[:2]][:1]

        if self.whose_move:
            if color != 'w': return
        else:
            if color != 'b': return
        
        if not self.isCheck:
            match self.chess_board[move[:2]][1:]:
                case 'K': listMoves = king(board=self.chess_board, position=move[:2], color=color, attacked_fields=[])
                case 'Q': listMoves = queen(board=self.chess_board, position=move[:2], color=color)
                case 'R': listMoves = rook(board=self.chess_board, position=move[:2], color=color)
                case 'B': listMoves = bishop(board=self.chess_board, position=move[:2], color=color)
                case 'S': listMoves = knight(board=self.chess_board, position=move[:2], color=color)
                case 'P': listMoves = pawn(board=self.chess_board, position=move[:2], color=color, lastMove='')
                case other: listMoves = []
        else:
            listMoves = king(board=self.chess_board, position=move[:2], color=color, attacked_fields=[])
            if listMoves == []:
                pass

        if move[2:4] in listMoves:
            self.chess_board[move[2:4]] = self.chess_board[move[:2]]
            self.chess_board[move[:2]] = '  '
        else: return

        if self.whose_move: self.whose_move = False 
        else: self.whose_move = True