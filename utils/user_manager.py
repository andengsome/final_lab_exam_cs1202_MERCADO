import os
from utils.user import *
from utils.dice_game import *

diceGame = DiceGame()

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

#funtion to open, read and iterate the users file inside the data directory
    def load_users(self):
        try:
            with open("data/users.txt", "r") as file:
                for line in file:
                    username, password = line.strip().split(",")
                    self.users[username] = password
        except FileNotFoundError:
            os.makedirs('data', exist_ok=True)
            print("File not found. Created 'data' directory.")
        except Exception as e:
            print(f"Error reading file: {e}")

#function that saves the entered username and password to users file                 
    def save_users(self):
        try:
            with open("data/users.txt", "w") as file:
                for username, password in self.users.items():
                    file.write(f"{username},{password}\n")
        except Exception as e:
            print(f"Error occurred while saving users: {e}")

#function that checks the username
    def validate_username(self, username):
        if len(username) >= 4:
            if username not in self.users:
                return True
            else:
                print("Username already exists.")
        else:
            print("Username must be at least 4 characters long.")

#function that checks the password
    def validate_password(self, password):
        if len(password) >= 8:
            return True
        else:
            print("Password must be at least 8 characters long.")

#function to register user
    def register(self):
        while True:
            username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
            if not username.strip():
                print("Canceled.")
                return
            password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
            if not password.strip():
                print("Canceled.")
                return
            
            if self.validate_username(username) and self.validate_password(password):
                if username in self.users:
                    print("Username already exists.")
                else: 
                    self.users[username] = {"password": password}
                    self.save_users()
                    print("Registration successful.")
                    return True
            else:
                print("Registration failed. Please try again.")
                return False

#funtion to login user
    def login(self):
        print("\nLogin")
        username = input("Enter username, or leave blank to cancel: ")
        if not username.strip():
            print("Login failed.")
            return
        if username in self.users:
            password = input("Enter password, or leave blank to cancel: ")
            if not password.strip():
                print("Login canceled.")
                return 

            if self.users[username]["password"] == password:
                print("Logged in successfully.")
                diceGame.game_menu(username)
            else:
                print("Invalid username or password.")
                return
        else:
            print("Username does not exist.")
            return