import os
import random
from utils.user_manager import UserManager
from utils.score import Score

class DiceGame:
    def __init__(self):
        self.user_manager = UserManager()
        self.scores = []
        self.current_user = None
        self.load_scores()
    
    def load_scores(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('data/rankings.txt'):
            with open('data/rnkings.txt', 'w') as file:
                pass
        else:
            with open('data/rankings.txt', 'r') as file:
                for line in file:
                    if line.strip():
                        username, game_id, points, wins = line.strip().split(',')
                        self.scores.append(Score(username,int(game_id), int(points), int(wins)))
    
    def save_scores(self, score):
        with open('data/rankings.txt', 'a') as file:
            file.write(f"{score.username},{score.game_id},{score.points},{score.wins}\n")
            
            self.scores.append(score)
            self.scores.sort(key=lambda x: x.points, reverse=True)
            self.scores = self.scores[:10]
            with open('data/rankings.txt', 'w') as file:
                for scores in self.scores:
                    file.write(f"{scores.username},{score.game_id},{score.points},{score.wins}\n")
    
    def play_game(self):
       print("Starting game as {self.current_user.username}...")
       total_points = 0
       stages_won = 0
       game_id = len(self.scores) + 1
       
       while True:
           round_points = 0
           player_wins = 0
           cpu_wins = 0
           
           while player_wins < 2 and cpu_wins < 2:
               player_roll = random.randint(1,6)
               cpu_roll = random.randint(1,6)
               print(f"{self.current_user.username} rolled: {player_roll}\nCPU rolled: {cpu_roll}")
               
               if player_roll > cpu_roll:
                   player_wins += 1
                   round_points += 1
                   print(f"You won this round, {self.current_user.username}!")
               elif player_roll < cpu_roll:
                   cpu_wins += 1
                   print("CPU wins this round!")
               else:
                   print("It's a tie!")
                   
                   if player_wins == 3:
                       round_points += 3
                       total_points += round_points
                       stages_won += 1
                       print(f"You won this stage, {self.current_user.username}!\nTotal points: {total_points}\nStages won: {stages_won}")
                       break
                   elif cpu_wins == 3:
                       print("Game over. You didn't win any stages.")
                       return
                   
                   choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
                   if choice == '0':
                       break
                   elif choice != '1':
                       print("Invalid input. Pllease enter 1 for Yes or 0 for No.")
                       
                       score = Score(self.current_user.username, game_id, total_points, stages_won)
                       if stages_won > 0:
                           self.save_scores(score)
                           
    def show_top_scores(self):
        if not self.scores:
            print("\nNo games played yet. Play a game to see top scores.")
            return
        print("TOP SCORES PAGE")
        for score in self.scores:
            print(f"{score.username} - Points: {score.points}, Wins: {score.wins}")
    
    def logout(self):
        self.current_user = None

	def menu():
		pass