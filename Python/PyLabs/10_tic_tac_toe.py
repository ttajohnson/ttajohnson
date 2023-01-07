# LAB 10: TIC TAC TOE
# write a Player class and Game class to model Tic Tac Toe, and a function main
# that models gameplay taking in user inputs through REPL.

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# >>>
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

    def calc_winner(self, player):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == player.token:
            return player.token
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == player.token:
            return player.token
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == player.token:
            return player.token
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == player.token:
            return player.token
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == player.token:
            return player.token
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == player.token:
            return player.token
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == player.token:
            return player.token
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == player.token:
            return player.token
        else:
            return None

    def is_full(self):
        for _ in self.board:
            if any(item == "-" for item in _):
                return False
        return True

    def is_game_over(self, player):
        return self.calc_winner(player) or self.is_full()


def Main():

    while True:

        game = Game()

        print("Welcome to Tic Tac Toe!")

        player_one = Player(
            input("Player One Name: ").title(), input("Player One Token: ").upper()
        )
        player_two = Player(
            input("Player Two Name: ").title(), input("Player Two Token: ").upper()
        )

        turn = 0

        while True:

            player = player_one if turn % 2 == 0 else player_two

            print(game.__repr__())

            while True:
                x = int(input(f"{player.name}, place {player.token} in which row: "))
                y = int(input(f"{player.name}, place {player.token} in which column: "))
                if game.board[x][y] != "-":
                    print("Space already claimed...")
                else:
                    game.move(x, y, player)
                    break
            if game.calc_winner(player) == player.token:
                print(game.__repr__())
                print(f"{player.name} has won the game!")
                break

            elif game.is_full() == True:
                print(game.__repr__())
                print("The game was a draw!")
                break

            turn += 1

        if game.is_game_over(player) == True or player.token:
            another_game = input("Want to play again? Y/N ").upper()
            if another_game == "N":
                break


Main()
# >>>
