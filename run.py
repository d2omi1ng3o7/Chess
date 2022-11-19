from src.main import ChessGame
from src.constants import CHESS_BOARD

if __name__ == '__main__':
    game = ChessGame(CHESS_BOARD)
    while True:
        # game.clearScreen()
        game.printChessBoard()
        listAllMoves = game.getMoves()
        game.move(listAllMoves)


# skoczki, gońce, wierze, hetmany, piony chyba działają już w pełni
# do poprawy króle
# zrobić szach mat i pat i bicie w przelocie
