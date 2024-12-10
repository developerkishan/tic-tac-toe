import random 
# user_action = input("Enter a choice(rock, paper, scissors): ")
# possible_actions = ["rock","paper","scissors"]
# computer_action = random.choice(possible_actions)
# print(f"You chose {user_action} , computer chose {computer_action}")
# if computer_action == "rock":
#     if user_action == "paper":
#         print("User wins ")
#     elif user_action == "scissors":
#         print("computer wins ")
# elif computer_action == "paper":
#     if user_action == "rock":
#         print("Computer wins ")
#     elif user_action == "scissors":
#         print("User wins ")
# elif computer_action == "scissors":
#     if user_action == "rock":
#         print("Computer loose ")
#     elif user_action == "paper":
#         print("User loose ")
# else:
#     print("The game is draw")

def play():
    user_choice = input("Enter a choice 'r' for rock , 'p' for paper , 's' for scissors : \n")
    computer_choice = random.choice(["r","p","s"])

    if user_choice == computer_choice:
        return "that's a tie"
    if iswin(user_choice, computer_choice):
        return "You win"

    return "You loose"

def iswin(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player =='s' and opponent =='p'):
        return True
    

print(play())