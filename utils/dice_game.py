import os
import random
from datetime import datetime
from utils.score import *
from utils.user import *


class DiceGame:
    def __init__(self):
        self.scores = {}
        self.users = {}
        self.current_users = None
        self.load_scores()

    def load_scores(self):
        try:
            with open("data/rankings.txt", "r") as file:
                for rank in file:
                    data = rank.strip().split(', ')
                    if len(data) == 4:
                        username, game_id, points, wins = data
                        self.scores[len(self.scores)] = {'username': username, 'game_id': int(game_id), 'points': int(points), 'wins': int(wins)}
                    else:
                        print(f"Ignore line: {rank.strip()} - Insufficient data")
        except FileNotFoundError:
            os.makedirs('data', exist_ok=True)
            print("File not found. Created 'data' directory.")
        except Exception as e:
            print(f"Error reading file: {e}")

    def save_score(self, username, points, wins):
        game_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
        try:
            with open("data/rankings.txt", "a") as file:
                file.write(f"{username},{game_id},{points},{wins}\n")
        except FileNotFoundError:
            print("Error: Could not save score. File not found.")

    def play_game(self, username):
        while True:
            self.score = 0
            self.stages_won = 0
            print(f"\nStarting game as {username}...")
            while True:
                self.wins = 0
                print(f"\nLet the game begins!")

                for roll in range(3): 
                    user_roll = random.randint(1, 6)
                    cpu_roll = random.randint(1, 6)
                    print(f"{username} rolled: {user_roll}")
                    print(f"CPU rolled: {cpu_roll}")

                    if user_roll > cpu_roll:
                        print(f"You win this round, {username}!")
                        self.score += 1
                        self.wins += 1
                    elif user_roll < cpu_roll:
                        print("CPU wins this round!")
                    else:
                        print("It's a tie!")

                if self.wins >= 2:
                    self.score += 3
                    self.stages_won += 1
                    print(f"You won this stage, {username}!")
                    print(f"Total Points: {self.score} pts, Stages Won: {self.stages_won}")
                    try:     
                        choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
                        if choice == "1":
                            continue
                        elif choice == "0":
                            print(f"Game over. You won {self.stages_won} stages with a total of {self.score} points.")
                            self.save_score(username, self.score, self.stages_won)
                            self.dice_menu(username)
                            return False
                        else:
                            print("Invalid input. Please enter 1 for Yes and 0 for No.")
                    except Exception as e:
                        print(f"Error occured: {e}")
                else:
                    print(f"You lost this stage, {username}.")
                    print("Game over. You didn't win any stages.")
                    self.dice_menu(username)
                    return

                print(f"Total Points: {self.score}, Stages won: {self.stages_won}")
                self.dice_menu(username)

    def show_top_scores(self, username):
        try:
            with open("data/rankings.txt", "r") as file:
                scores = [line.strip().split(",") for line in file.readlines()]
                scores.sort(key=lambda x: int(x[2]), reverse=True)
                print("\nTop 10 Scores:")
                for i, score in enumerate(scores[:10], start=1):
                    if len(score) >= 4:
                        print(f"{i}. Username: {score[0]}: Points - {score[2]}, Wins - {score[3]}")
                    else:
                        print("No games played yet. Play a game to see top scores.")
                        return
            self.dice_menu(username)
        except FileNotFoundError:
            print("No scores recorded yet.")
            return

    def logout(self):
        self.current_users = None

    def dice_menu(self, username):
        print(f"\nWelcome, {username}!")
        print("Menu: ")
        print("1. Start Game")
        print("2. Show Top Scores")
        print("3. Log out")
        user_choice = input("Enter your choice, or leave blank to cancel: ")
        if not user_choice.strip():
            print("Canceled.")
            return
        else: 
            if user_choice == "1":
                self.play_game(username)
            elif user_choice == "2":
                self.show_top_scores(username) 
            elif user_choice == "3":
                print(f"'Til we play again, {username}!")
                print("\nYou logged out successfully.")
                self.logout()
            else:
                print("Invalid choice.")