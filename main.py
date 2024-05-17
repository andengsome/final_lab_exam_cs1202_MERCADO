from utils.user_manager import *

go = UserManager()

def main():
    go.load_users()
    while True:
        
        print("\nWelcome to Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            go.register()
        elif choice == "2":
            go.login()
        elif choice == "3":
            print("Exiting the game. Good bye!")
            break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()