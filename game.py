from random import choice


class RockPaperScissors:
    # Each key corresponds to a move that is beaten by its value.
    bested_moves = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }
    # Dictionary of users and their ranks loaded from 'rating.txt'.
    stats = {}

    def __init__(self):
        self._get_stats()

    def get_winner(self, c_move, p_move):
        """Determines the winner and rewards points."""
        if self.bested_moves[c_move] == p_move:
            print(f"Well done. The computer chose {c_move} and failed")
            return 100
        elif self.bested_moves[p_move] == c_move:
            print(f"Sorry, but the computer chose {c_move}")
            return 0
        elif c_move == p_move:
            print(f"There is a draw {c_move}")
            return 50

    def _get_stats(self):
        """Reads file and converts contents into dictionary."""
        with open('rating.txt') as file:
            for line in file:
                (key, val) = line.split()
                self.stats[key] = int(val)
        file.close()

    def find_user(self, user):
        """Finds user in stats dictionary. If not found, creates entry."""
        if user in self.stats.keys():
            return self.stats[user]
        else:
            self.stats[user] = 0

    def add_points(self, user, points):
        """Adds points to user's rank."""
        self.stats[user] += points

    def game(self):
        """Main game loop."""
        user = input("Enter your name: ")
        print(f"Hello, {user}")
        while True:
            # Randomly selects move (and beating move) for computer.
            computer_move = choice(list(self.bested_moves.keys()))
            # Get user input as long as there is input.
            try:
                player_move = input()
            except EOFError:
                break
            # Checks if input matches any bested_moves keys.
            if player_move in self.bested_moves:
                result = self.get_winner(computer_move, player_move)
                self.add_points(user, result)
            # Checks for exit command.
            elif player_move == "!exit":
                print("Bye!")
                break
            # Checks for rating command.
            elif player_move == "!rating":
                print(f"Your rating: {self.stats[user]}")
            # Handles invalid inputs.
            else:
                print("Invalid input")


RockPaperScissors().game()
