from src.main import Chess

if __name__ == '__main__':
    game = Chess()
    while True:
        # game.clear_screen()
        game.printChessBoard()
        game.move()


# skoczki, gońce, wierze, hetmany, piony chyba działają już w pełni
# do poprawy króle
# zrobić szach mat i pat i bicie w przelocie