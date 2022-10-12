from . import constants as const
import os

class Chess():
    def __init__(self):
        self.chess_board = const.CHESS_BOARD
        self.whose_move = 'w'

    def printChessBoard(self):
        print('\n', '---------------------------------------------------------', sep='')
        counter = 1
        for i in self.chess_board:
            print(self.chess_board[i], end='', sep='')
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
        move = input()
        figure = self.chess_board[move[:2]]

        if figure[3:4] != self.whose_move:
            return

        if figure[3:4] == self.chess_board[move[2:4]][3:4]:
            return

        self.chess_board[move[:2]] = '|      '
        self.chess_board[move[2:4]] = figure

        if self.whose_move == 'w':
            self.whose_move = 'b'
        else:
            self.whose_move = 'w'