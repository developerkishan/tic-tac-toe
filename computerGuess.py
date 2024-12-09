import random
def random_number_function_user(x):
    random_number = random.randint(1,x)
    guessed_number = 0
    while(guessed_number != random_number):
        guessed_number = int(input(f"Guess a number between 1 and {x}: "))
        if guessed_number < random_number:
            print(f"Sorry , guess again. Too low.")
        elif guessed_number > random_number:
            print(f"Sorry , guess again . Too high")        
    print(f"Congratulations !! You have guessed it correctly .")
# def random_number_function_computer(x):
#     user_number = int(input(f"Guess a number between 1 and {x}: "))
#     computer_guessed_number = 0 
#     while(computer_guessed_number != user_number):
#         computer_guessed_number = random.randint(1,10)
#         if computer_guessed_number < user_number:
#             print(f"Sorry , guess again. Too low.")
#         elif computer_guessed_number > user_number:
#             print(f"Sorry , guess again . Too high")        
#     print(f"Congratulations !! You have guessed it correctly .")
# random_number_function_user(10)
# random_number_function_computer(10)

def computer_guess(x):
    low=1
    high=x
    feedback =''
    while feedback != 'c':
        guess_number = random.randint(low,high)
        print(guess_number)
        feedback = input(f"Is {guess_number} too high (h) , too low (l) , or correct (c)??")
        if feedback == 'h':
            high = guess_number-1
        elif feedback == 'L':
            low = guess_number+1
    print(f"Congratulations!! You guessed the number {guess_number}")
    
 
computer_guess(10)