class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


class Game(Player):
    def __init__(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def __repr__(self):
        row1 = "|".join(self.board[0])
        row2 = "|".join(self.board[1])
        row3 = "|".join(self.board[2])
        game_board = f"{row1}\n{row2}\n{row3}"
        return game_board

    def move(self, x, y, player):
        self.board[x][y] = player.token
