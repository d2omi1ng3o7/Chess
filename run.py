from src.main import Chess

if __name__ == '__main__':
    game = Chess()
    while True:
        # game.clear_screen()
        game.printChessBoard()
        game.move()