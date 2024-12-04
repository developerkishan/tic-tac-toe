import random
WELCOME_MESSGE = "Welcome to the Word Guessing Game!"
GOOD_GUESS_MESSAGE = "Good guess!"
INVALID_INPUT_MESSAGE = "Please enter a valid alphabet"
INVALID_LENGTH_MESSAGE = "Please enter only one alphabet character"
ALREADY_GUESSED_MESSAGE = "You've already guess the letter :"
INCORRECT_GUESS_MESSAGE = "Oops! That letter is not in the word."
GAME_WON_MESSAGE = "Congratulations! You guessed the word:"
GAME_OVER_MESSAGE = "Game over! The word was:"
REMAINING_ATTEMPTS_MESSAGE = "Remaining attempts:"
def print_status(attempts,display_word):
    print(f"{REMAINING_ATTEMPTS_MESSAGE} {attempts}" )
    print(' '.join(display_word))
def is_valid_input(guessed_char , guessed_chars):
    if not  guessed_char.isalpha():
        print(INVALID_INPUT_MESSAGE)
    if len(guessed_char) > 1:
        print(INVALID_LENGTH_MESSAGE)
    if guessed_char in guessed_chars:
        print(f"{ALREADY_GUESSED_MESSAGE} {guessed_char}")
        return False
    return True
def is_game_won(display_word,secret_word):
    if ''.join(display_word) == secret_word:
        return True
    return False
def main():
    words = ['badminton', 'coding', 'business', 'coach', 'sports', 'speaker']
    secret_word = random.choice(words)
    secret_word_dict = dict(enumerate(secret_word))
    guessed_chars = set()
    attempts = 8
    print(WELCOME_MESSGE)
    display_word = ['_' for i in range(len(secret_word))]
    print_status(attempts,display_word) 
    while (attempts > 0):
        guessed_char = input("Player inputs: ").lower()
        if not is_valid_input(guessed_char,guessed_chars):
            continue
        matching_indices = [key for key,value in secret_word_dict.items() if guessed_char == value]
        if matching_indices == []:
            print(INCORRECT_GUESS_MESSAGE)
            attempts-=1
            print_status(attempts,display_word)
        else:
            print(GOOD_GUESS_MESSAGE)
            for key in matching_indices:
                display_word[key]= guessed_char
                print_status(attempts,display_word)
        if is_game_won(display_word,secret_word):
            print(f"{GAME_WON_MESSAGE} {secret_word}")
            break
    if attempts ==0:
        print(f"{GAME_OVER_MESSAGE} {secret_word}")
if __name__ == "__main__":
    main()