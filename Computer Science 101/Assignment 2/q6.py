def get_player_guess(counter):
    user_input = input("Please enter your guess: ")
    while len(user_input) != 5 or user_input.isalpha() == False:
        user_input = input("Your guess must have 5 letters: ")
    counter+=1
    return user_input.lower(), counter

def map_words(correct):
    word_map = {}
    for i in list(correct):
        word_map[i] = 1 + (word_map[i] if i in word_map.keys() else 0)
    return word_map

def replace_characters(correct, guess, current_guess, map):
    for pos,character in enumerate(current_guess):
        if character == correct[pos]:
            map[character] -= 1
            guess[pos] = character.upper()
    for pos,character in enumerate(current_guess):
        if (character in correct and character != correct[pos]) and map[character] > 0:
                map[character] -= 1
                guess[pos] = character
    
def play_round(word):
    counter = 1
    solved = False
    guess = [ '_', '_', '_', '_', '_' ]
    while guess != list(word.upper()) and counter <= 6:
        print(f"Guess {counter}:\n")
        user_input, counter = get_player_guess(counter)
        a = map_words(word)
        replace_characters(list(word), guess, user_input, a)
        print(" ".join(guess) + '\n')
        if guess != list(word.upper()): 
            guess = [ '_', '_', '_', '_', '_' ]
        else:
            solved = True
    counter-=1
    return counter, solved
    
round_results = play_round("ghost")
print(f"Number of guesses: {round_results[0]}, Is solved? {round_results[1]}")