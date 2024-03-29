class Player:
    def __init__(self, name, token):
        self.name = input("What is your name: ")
        self.token = input("Choose your token: ")

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.token == other.token
        return False


class Game(Player):
    def __init__(self):
        # self.board = [
        #     ['-','-','-'], # 0,0 | 0,1 | 0,2
        #     ['-','-','-'], # 1,0 | 1,1 | 1,2
        #     ['-','-','-']  # 2,0 | 2,1 | 2,2

        #     # OR

        # ]
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def __repr__(self):
        # board_str = ''
        # for row in self.board:
        #     board_str += '|'.join(row) + '\n'
        # return board_str

        # # OR

        return '\n'.join(['|'.join(row) for row in self.board])



    def move(self, x, y, player):
        self.board[x][y] = Player.token

    def calc_winner(self):
        pass

    def is_full(self):
        if '-' in self.board:
            return False
        else:
            return True

    def is_game_over(self):
        pass

player1 = Player('merry', 'X')