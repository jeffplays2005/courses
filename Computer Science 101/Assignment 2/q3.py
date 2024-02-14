def get_player_guess():
    user_input = input("Please enter your guess: ")
    while len(user_input) != 5 or user_input.isalpha() == False:
        user_input = input("Your guess must have 5 letters: ")
    return user_input.lower()

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
    guess = [ '_', '_', '_', '_', '_' ]
    while guess != list(word.upper()):
        user_input = get_player_guess()
        a = map_words(word)
        replace_characters(list(word), guess, user_input, a)
        print(" ".join(guess))
        if guess != list(word.upper()): 
            guess = [ '_', '_', '_', '_', '_' ]
            print()

def print_banner():
    print("""========================================================================
                                 Rules
You have unlimited guesses to figure out the solution.
All solutions are words that are 5 letters long.
Letters that have been guessed correctly are displayed in uppercase.
Letters that are in the word but have been guessed in the wrong location
are displayed in lowercase.
========================================================================\n""")

def main():
    word = input("Enter word to guess: ")
    print()
    name = input("Please enter your name: ")
    print(f"\nWelcome to Wordle 101 {name}\n")
    print_banner()
    play_round(word)
    
main()