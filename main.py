from utils.dice_game import DiceGame

def menu():
    game = DiceGame()
    while True:
        if not game.current_user:
            print("Welcome to Dice Roll Game")
            print("1. Register")
            print("2. Log In")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
               game.user_manager.register()
            elif choice == "2":
                game.current_user = game.user_manager.login()
            elif choice == "3":
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print(f"\nWelcome, {game.current_user.username}!")
            print("Menu:")
            print("1. Start game")
            print("2. Show top scores")
            print("3. Logout")
            
            choice = input("Enter you choice, or leave it blank to cancel: ")
            
            if choice == '1':
                game.play_game()
            elif choice == '2':
                game.show_top_scores()
            elif choice == '3':
                game.logout()
            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    menu()
                