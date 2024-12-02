import random
words = ['badminton', 'coding', 'business', 'coach', 'sports', 'speaker']
secret_word = random.choice(words)
guessed_chars = set()
attempts = 8
print("Welcome to the word Guessing Game!")
display_word = ['_' for i in range(len(secret_word))]
print(''.join(display_word))
print(f"Remaining attempts: {attempts}" )
while (attempts > 0):
    guessed_char = input("Player inputs: ")
    guessed_chars.add(guessed_char)
    is_found = 'no'

    for count in range(len(secret_word)):
        if guessed_char == secret_word[count]:
            display_word[count]= guessed_char
            print("Good guess!")
            print(''.join(display_word))
            print(f"Remaining attempts: {attempts}" )
            is_found = 'yes'
    if is_found == 'no':
        print("Oops! That letter is not in the word.")
        print(''.join(display_word))
        attempts-=1
        print(f"Remaining attempts: {attempts}" )
    
    if ''.join(display_word) == secret_word:
        print("Congratulations! You guessed the word:", secret_word)
        break
if attempts ==0:
    print("Game over! The word was:", secret_word)
