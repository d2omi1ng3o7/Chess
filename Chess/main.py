from . import constants as const
import os

class Chess():
    def __init__(self):
        self.chess_board = const.CHESS_BOARD

    def printChessBoard(self):
        print()
        print('---------------------------------------------------------')
        counter = 1
        for i in self.chess_board:
            print(self.chess_board[i], end='', sep='')
            if counter == 8:
                print('|', end='')
                print()
                print('---------------------------------------------------------')
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
        move = input()
        piece = self.chess_board[move[:2]]
        self.chess_board[move[:2]] = '|      '
        self.chess_board[move[2:4]] = piece


