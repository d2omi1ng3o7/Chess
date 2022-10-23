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

    def printChessBoard(self):
        print('\n', '---------------------------------------------------------', sep='')
        counter = 1
        for i in self.chess_board:
            print(f'|  {self.chess_board[i]}  ', end='', sep='')
            if counter == 8:
                print('|', end='')
                print('\n', '---------------------------------------------------------', sep='')
                counter = 1
            else:
                counter += 1
        print()
    
    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def move(self):   

        if self.whose_move:
            move = input()

            if self.chess_board[move[:2]][:1] != 'w': return

            if self.chess_board[move[:2]][1:] == 'K':
                listMoves = king(position=move[:2], color='w', attacked_fields=[])
            elif self.chess_board[move[:2]][1:] == 'Q':
                listMoves = queen(position=move[:2], color='w')
            elif self.chess_board[move[:2]][1:] == 'R':
                listMoves = rook(position=move[:2], color='w')
            elif self.chess_board[move[:2]][1:] == 'B':
                listMoves = bishop(position=move[:2], color='w')
            elif self.chess_board[move[:2]][1:] == 'S':
                listMoves = knight(position=move[:2], color='w')
            elif self.chess_board[move[:2]][1:] == 'P':
                listMoves = pawn(position=move[:2], color='w', lastMove='')
            else:
                listMoves = []

            if move[2:4] in listMoves:
                self.chess_board[move[2:4]] = self.chess_board[move[:2]]
                self.chess_board[move[:2]] = '  '
            else: return

            self.whose_move = False
       
        else:
            move = input()

            if self.chess_board[move[:2]][:1] != 'b': return

            if self.chess_board[move[:2]][1:] == 'K':
                listMoves = king(position=move[:2], color='b', attacked_fields=[])
            elif self.chess_board[move[:2]][1:] == 'Q':
                listMoves = queen(position=move[:2], color='b')
            elif self.chess_board[move[:2]][1:] == 'R':
                listMoves = rook(position=move[:2], color='b')
            elif self.chess_board[move[:2]][1:] == 'B':
                listMoves = bishop(position=move[:2], color='b')
            elif self.chess_board[move[:2]][1:] == 'S':
                listMoves = knight(position=move[:2], color='b')
            elif self.chess_board[move[:2]][1:] == 'P':
                listMoves = pawn(position=move[:2], color='b', lastMove='')

            if move[2:4] in listMoves:
                self.chess_board[move[2:4]] = self.chess_board[move[:2]]
                self.chess_board[move[:2]] = '  '
            else: return      

            self.whose_move = True