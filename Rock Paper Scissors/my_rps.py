# termcolor==2.3.0 "python3 -m pip install --upgrade termcolor"
# ascii_magic==2.3.0 "pip install ascii_magic"

from termcolor import colored
from ascii_magic import AsciiArt
import random
import os
os.system("color")


moves = ["rock", "paper", "scissors"]


class Player:
    def __init__(self, score=0):
        self.score = score
        self.moves = ["rock", "paper", "scissors"]

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        choice = input("Enter your move: ")
        if choice in moves:
            return choice
        else:
            print(colored("Pick a valid move!", "red", "on_yellow"))
        return self.move()

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def move(self):
        if len(self.__dict__.keys()) == 2:
            self.my_move = random.choice(self.moves)
            return self.my_move
        elif len(self.__dict__.keys()) > 2:
            print(self.my_move)
            return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = their_move
        return self.my_move


class CyclePlayer(Player):
    def move(self):
        if len(self.__dict__.keys()) == 2:
            return random.choice(self.moves)
        else:
            if self.my_move in self.moves:
                index = self.moves.index(self.my_move)
                cycle_list = [i for i in range(2) for i in self.moves]
                return cycle_list[index + 1]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        return my_move


def beats(one, two):
    return ((one == "rock" and two == "scissors") or
            (one == "scissors" and two == "paper") or
            (one == "paper" and two == "rock"))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}  Player 2 played {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.p1.score += 1
            print(f"You beat Player 2! You now have {self.p1.score} point(s) "
                  f"and player 2 has {self.p2.score} points!")
        elif beats(move2, move1):
            self.p2.score += 1
            print(f"Player 2 beat you! You have {self.p1.score} point(s) "
                  f"and player 2 now has {self.p2.score} points!")
        else:
            print("You tied! Play again! "
                  f"The score is still {self.p1.score} - {self.p2.score}.")

    def play_game(self):
        print(colored("Game start!", "white", "on_blue"))
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print(colored(f"You won! The final score was"
                          f" {self.p1.score} - {self.p2.score}", "green"))
        elif self.p1.score < self.p2.score:
            print(colored(f"You lost! The final score was"
                          f" {self.p1.score} - {self.p2.score}", "red"))
        else:
            print(colored(f"You tied! The final score was"
                          f" {self.p1.score} - {self.p2.score}", "yellow"))

        print("Game over! Play again? Please enter yes or no.")
        while True:
            choice = input()
            if choice == "yes":
                self.play_game()
            elif choice == "no":
                print("Thanks for playing!")
                my_art = AsciiArt.from_url("https://github.com/chadhansonsr/Udacity-Python/blob/main/rps.jpg?raw=true")  # noqa
                my_art.to_terminal()
                quit()
            else:
                print(colored("Sorry, I don't understand. "
                              "Would you like to play again? "
                              "Please enter yes or no.", "red", "on_yellow"))


if __name__ == '__main__':
    print("Enter your opponents style of play: \n"
          "all rocks \n"
          "random \n"
          "human \n"
          "reflect \n"
          "cycle")
    while True:
        choice = input()
        if choice == "all rocks":
            game = Game(HumanPlayer(), Player())
            game.play_game()
        elif choice == "random":
            game = Game(HumanPlayer(), RandomPlayer())
            game.play_game()
        elif choice == "human":
            game = Game(HumanPlayer(), HumanPlayer())
            game.play_game()
        elif choice == "reflect":
            game = Game(HumanPlayer(), ReflectPlayer())
            game.play_game()
        elif choice == "cycle":
            game = Game(HumanPlayer(), CyclePlayer())
            game.play_game()
        else:
            print(colored("Sorry, I don't understand. "
                  "Please enter a valid style of play.", "red", "on_yellow"))
