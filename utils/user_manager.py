class UserManager:
	def load_users():
		pass

	def save_users():
		pass

	def validate_username():
		pass

	def validate_password():
		pass

    def register():
        while True:
            try:
                print("REGISTER PAGE")
                username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
                password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
                if len(password) >= 8:
                    if username in acc_lib:
                        print("Username already exists.")
                    else:
                        print("Account registered successfully.")
                        acc_lib[username] = {
                            "username": username,
                            "password": password,
                            "Balance": 0,
                            "Points": 0,
                            "rented_games": []
                        }
                        menu()
                else:
                    print("Password must be at least 8 characters long.")
            except ValueError:
                print("Invalid input.")
            
def login():
	pass