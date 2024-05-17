import os
from utils.user import User
class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()
        
    def load_users(self):
        if not os.path.exists('data'):
            os.makedirs('data')
            if not os.path.exists('data/users.txt'):
                with open('data/users.txt', 'w') as file;
                pass
            else:
                with open('data/users.txt', 'r') as file:
                    for line in file:
                        if line.strip():
                            username, password= line.strip().split(',')
                            self.users[username] = User(username, password)
    def save_users(self):
        with open('data/users.txt', 'w') as file:
            for user in self.users.values():
                file.write(f"{user.username},{user.password}\n")

    def validate_username(self, username):
        return len(username) >= 4

    def validate_password(self, password):
        return len(password) >= 8
    
    def register(self):
        print("REGISTRATION PAGE")
        while True:
           username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
           if not username:
               return
           if not self.validate_username(username):
               print("Username must be at least 4 characters long.")
               continue
           if username in self.users:
               print("Username already exists. Please try another one.")
               continue
           break
        while True:
            password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
            if not password:
                return
            if not self.validate_password(password):
                print("Password must be at least 8 characters long.")
                continue
            break
        
        user = User(username, password)
        self, users[username] = user
        self, save_users()
        print("Registration succesful.")
            
    def login():
        print("LOGIN PAGE")
        username = input("Enter username, or leave blank to cancel: ")
        if not username:
            return None
        password = input("Enter password, or leave blank to cancel: ")
        if not password:
            return None
        
        user = self.users.get(username)
        if user and user.password == password:
            print("Login successful.")
            return user
        else:
            print("Invalid username or password. Please try again.")
            return None