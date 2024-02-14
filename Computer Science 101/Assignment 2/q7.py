import random

def get_player_guess(counter):
    user_input = input("Please enter your guess: ")
    while len(user_input) != 5 or user_input.isalpha() == False:
        user_input = input("Your guess must have 5 letters: ")
    counter+=1
    return user_input.lower(), counter

def map_words(correct):
    word_map = {}
    for i in list(correct):
        if i in word_map.keys():
            word_map[i] += 1
        else:
            word_map[i] = 1
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

def print_banner():
    name = input("Please enter your name: ")
    print(f"\nWelcome to Wordle 101 {name}\n")
    print("""========================================================================
                                 Rules
You have 6 guesses to figure out the solution.
All solutions are words that are 5 letters long.
Letters that have been guessed correctly are displayed in uppercase.
Letters that are in the word but have been guessed in the wrong location
are displayed in lowercase.
========================================================================\n""")

def get_word_file():
    file = open(input("Enter the name of the word file: "))
    lines = file.read().split('\n')
    words = []
    for i in lines:
        if len(i.strip()) > 0:
            words.append(i.strip())
    return words

def print_bar_chart(data_dict):
    for i in sorted(data_dict.keys()):
        has_chars = data_dict[i] * "#"
        print(f"{i}|{has_chars}{data_dict[i]}")

def print_summary(win_count, mapped_wins):
    print("""\n========================================================================
                                Summary""")
    # win percentage
    percentage = int(round((win_count['wins'] / (win_count['wins'] + win_count['loses']))  * 100))
    print(f"Win percentage: {percentage}%")
    # win distribution
    print("Win Distribution:")
    print_bar_chart(mapped_wins)
    print("========================================================================")

def parse_output(output, word, mapped_wins, win_count):
    if output[1] == True:
        print(f"Success! The word is {word}!\n")
        mapped_wins[output[0]] += 1
        win_count['wins'] += 1
    else:
        print(f"Better luck next time! The word is {word}!\n")
        win_count['loses'] += 1
        
def main():
    round = 1
    restart = "Y"
    possible_words = get_word_file()
    print_banner()
    mapped_wins = { 1:0, 2:0, 3:0, 4:0, 5:0, 6:0 }
    win_count = { 'wins': 0, 'loses': 0 }
    while restart == 'Y':
        word = get_random_word(possible_words)
        print(f"\nRound: {round}\n")
        output = play_round(word)
        parse_output(output, word, mapped_wins, win_count)
        restart = input("Please enter 'Y' to continue or 'N' to stop playing: ")
        while restart not in ['Y', 'N']:
            print("Only enter 'Y' or 'N'!")
            restart = input("Please enter 'Y' to continue or 'N' to stop playing: ")
        round += 1
    print_summary(win_count, mapped_wins)
    
# test
def get_random_word(words):
    random_index = random.randrange(len(words))
    return words[random_index]
random.seed(30)
main()