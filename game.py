from random import choice


def get_winner(move_set, c_move, p_move):
    """Determines the winner based on the move set and rewards points."""
    if c_move in move_set[p_move]:
        print(f"Well done. The computer chose {c_move} and failed")
        return 100
    elif p_move in move_set[c_move]:
        print(f"Sorry, but the computer chose {c_move}")
        return 0
    elif c_move == p_move:
        print(f"There is a draw ({c_move})")
        return 50


class RockPaperScissors:
    # Normal rock/paper/scissors moves
    normal_winning_moves = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    # Advanced moves
    advanced_winning_cases = {
        'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
        'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
        'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
        'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
        'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
        'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
        'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
        'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
        'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
        'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
        'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
        'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
        'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
        'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
        'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    }
    # Dictionary of users and their ranks loaded from 'rating.txt'.
    stats = {}

    def __init__(self):
        self._get_stats()

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

    def select_moveset(self, move_set):
        """Returns moveset specified by user."""
        if move_set == "":
            return self.normal_winning_moves
        elif move_set == "rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire":
            return self.advanced_winning_cases

    def game(self):
        """Main game loop."""
        user = input("Enter your name: ")
        print(f"Hello, {user}")
        move_set = self.select_moveset(input())
        print("Okay, let's start")
        while True:
            # Randomly selects move (and beating move) for computer.
            computer_move = choice(list(move_set.keys()))
            # Get user input as long as there is input.
            try:
                player_move = input()
            except EOFError:
                break
            # Checks if input matches any bested_moves keys.
            if player_move in move_set:
                result = get_winner(move_set, computer_move, player_move)
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
