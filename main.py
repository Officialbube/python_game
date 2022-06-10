import random

possible_actions = ["R","P","S"]


while True:
    computer_action = random.choice(possible_actions)
    user_action = input("Enter a choice (R, P, S): ").upper()

    if user_action == computer_action:
        print(f"Player({user_action}) : CPU({computer_action})")
        print(f"Both players selected {user_action}. It's a tie!")
        continue
    else:
        if user_action == "R":
            if computer_action == "S":
                print(f"Player ({user_action}) : CPU ({computer_action})")
                print("Rock smashes scissors! you win!")
            else:
                print(f"Player ({user_action}) : CPU ({computer_action})")
                print("paper covers rock! you lose.")        
        elif user_action == "P":
            if computer_action == "R":
                print(f"Player ({user_action}) : CPU ({computer_action})")
                print("paper covers rock! you win!")
            else:
                print(f"Player ({user_action}) : CPU ({computer_action})")
                print("scissors cuts paper! you loose.")
        elif user_action == "S":
            if computer_action == "P":
                print(f"Player ({user_action}) : CPU ({computer_action})")
                print("scissors cuts paper! you win!")
            else:
                print(f"Player ({user_action}) : CPU ({computer_action})")
                print("rock smashes scissors! you lose")       
        else:
            print("Error! You entered an invalid option")
            continue
    break