from constants import CHESS_BOARD


class Queen:
    def __init__(self):
        pass

    def moveList(self, position='45', color='w'):

        listWithMoves = []

        for x in range(int(position[:1])-1, 0, -1):
            new_position = f'{x}{position[1:]}'
            if '  ' != CHESS_BOARD[new_position]:
                if color != CHESS_BOARD[new_position][:1]:
                    listWithMoves.append(new_position)
                break
            listWithMoves.append(new_position)

        for x in range(int(position[:1])+1, 9):
            new_position = f'{x}{position[1:]}'
            if '  ' != CHESS_BOARD[new_position]:
                if color != CHESS_BOARD[new_position][:1]:
                    listWithMoves.append(new_position)
                break
            listWithMoves.append(new_position)

        for x in range(int(position[1:])-1, 0, -1):
            new_position = f'{position[:1]}{x}'
            if '  ' != CHESS_BOARD[new_position]:
                if color != CHESS_BOARD[new_position][:1]:
                    listWithMoves.append(new_position)
                break
            listWithMoves.append(new_position)

        for x in range(int(position[1:])+1, 9):
            new_position = f'{position[:1]}{x}'
            if '  ' != CHESS_BOARD[new_position]:
                if color != CHESS_BOARD[new_position][:1]:
                    listWithMoves.append(new_position)
                break
            listWithMoves.append(new_position)

        for x in range(1, max(8-int(position[:1]), int(position[1:])-1)+1):
            new_position = f'{str(int(position[:1])-x)}{str(int(position[1:])+x)}'
            if '  ' != CHESS_BOARD[new_position]:
                if color != CHESS_BOARD[new_position][:1]:
                    listWithMoves.append(new_position)
                break
            listWithMoves.append(new_position)

        for x in range(1, max(8-int(position[:1]), 8-int(position[1:]))+1):
            new_position = f'{str(int(position[:1])+x)}{str(int(position[1:])+x)}'
            if '  ' != CHESS_BOARD[new_position]:
                if color != CHESS_BOARD[new_position][:1]:
                    listWithMoves.append(new_position)
                break
            listWithMoves.append(new_position)

        for x in range(1, max(int(position[:1])-1, 8-int(position[1:]))+1):
            new_position = f'{str(int(position[:1])+x)}{str(int(position[1:])-x)}'
            if '  ' != CHESS_BOARD[new_position]:
                if color != CHESS_BOARD[new_position][:1]:
                    listWithMoves.append(new_position)
                break
            listWithMoves.append(new_position)

        for x in range(1, max(int(position[:1])-1, int(position[1:])-1)+1):
            new_position = f'{str(int(position[:1])-x)}{str(int(position[1:])-x)}'
            if '  ' != CHESS_BOARD[new_position]:
                if color != CHESS_BOARD[new_position][:1]:
                    listWithMoves.append(new_position)
                break
            listWithMoves.append(new_position)

        return listWithMoves