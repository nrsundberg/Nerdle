# Packages needed
from colorama import Fore
import csv
from random import sample

# Variables to instantiate
    # all words and answers list
all_words = {"words": []}
possible_words = {"words": []}
possible_words_scored = []
possible_words_refined = []
words = []
import_answers = []    
possible_answers = []
answer = []
    # create letter dictonaries (positional)
letter_one = []
letter_two = []
letter_three = []
letter_four = []
letter_five = []
    # create lists to hold the letter with count combined
letter_one_score = []
letter_two_score = []
letter_three_score = []
letter_four_score = []
letter_five_score = []
    # create dict for letter (key) and score (value)
letter_one_score_ranked = {}
letter_two_score_ranked = {}
letter_three_score_ranked = {}
letter_four_score_ranked = {}
letter_five_score_ranked = {}
    # List of lists to itterate through when ranking values
        # List for all letters in positions of words
list_letter = ["letter_one", "letter_two", "letter_three", "letter_four", "letter_five"]
        # List of all letters scored (duplicates)
list_score = ["letter_one_score", "letter_two_score", "letter_three_score", "letter_four_score", "letter_five_score"]
        # Dictonary of letters (key) and score (value)
dict_letters_score = ["letter_one_score_ranked", "letter_two_score_ranked", "letter_three_score_ranked", "letter_four_score_ranked", "letter_five_score_ranked"]
# Color list for print out of guess letters
color_list = [Fore.WHITE, Fore.WHITE, Fore.WHITE, Fore.WHITE, Fore.WHITE]


# Read in possible word list
with open('words_dictonary.csv', 'r') as read_obj:
    read = csv.reader(read_obj)
    words = list(read)
for lists in words:
    for word in lists:
        all_words["words"].append(word)
index_FALSE = all_words["words"].index("FALSE")
all_words["words"][index_FALSE] = "false"
# Read in possible answer list
with open('answers.csv', 'r') as read_obj:
        read = csv.reader(read_obj)
        import_answers = list(read)
for lists in import_answers:
    for word in lists:
        possible_answers.append(word)

def seprate_letters_from_words(word_list):
    for lists in list_letter:
        globals()[lists] = []
    for word in word_list:
        letter_index = 0
        for letter in word:
            globals()[list_letter[letter_index]].append(letter)
            letter_index = letter_index + 1

def get_letter_rank(letter):
    rank = float(letter[:-2])
    return rank

def get_word_rank(word):
    rank = float(word[:-6])
    return rank

def rank_letters_word_frequency():
    list_index = 0
    for lists in list_score:
        globals()[lists] = list(set(globals()[list_letter[list_index]]))
        for letter in globals()[lists]:
            globals()[dict_letters_score[list_index]][letter] = globals()[list_letter[list_index]].count(letter)
        list_index = list_index + 1

def rank_words():
    global possible_words_scored, possible_words_refined
    possible_words_scored = []
    possible_words_refined = []
    for word in possible_words["words"]:
        word_score = []
        letter_index = 0
        for letter in word:
            word_score.append(globals()[dict_letters_score[letter_index]][letter])
            if letter_index == 4:
                total_score = sum(word_score)
                possible_words_scored.append(f"{total_score}.{word}")
            letter_index = letter_index + 1
    possible_words_scored.sort(key= get_word_rank, reverse= True)
    for word in possible_words_scored:
        possible_words_refined.append(word[len(word)-5:])
    total_words = len(possible_words_refined)
    print(f"Total words left: {total_words}")
    if total_words < 10:
        print(possible_words_refined)
    else:
        print("Word suggestions:\n", possible_words_refined[0:5])

def new_answer():
    global answer
    answer = sample(possible_answers , k= 1)
    for word in answer.copy():
        answer = []
        for letter in word:
            answer.append(letter)

def game_without_letters_filter():
    letter_index = 0
    for letter in guess:
        if letter == answer[letter_index]:
            color_list[letter_index] = Fore.GREEN
            letter_index += 1
        elif letter in answer:
            color_list[letter_index] = Fore.YELLOW
            letter_index += 1
        else:
            color_list[letter_index] = Fore.BLACK
            letter_index += 1
    print(color_list[0] + guess[0] + color_list[1] + guess[1] + color_list[2] + guess[2] + color_list[3] + guess[3] + color_list[4] + guess[4] + Fore.RESET)

def call_guess_with_question():
    global guess
    guess = input("Please guess a word ")
    while guess not in possible_words["words"]:
        guess = input(Fore.RED + "Please guess a valid 5-letter word " + Fore.RESET)
    guess = [*guess]

def call_guess_without_question():
    global guess
    guess = input("")
    while guess not in possible_words["words"]:
        guess = input("")
    guess = [*guess]

def initial_refined_words():
    seprate_letters_from_words(all_words["words"])
    rank_letters_word_frequency()
    rank_words()

def ranking_refined_words():
    seprate_letters_from_words(possible_words["words"])
    rank_letters_word_frequency()
    rank_words()

# need to add something to count occurances of letters in answer and if > 2 change output color and if one and guessed twice can second letter
# and (len(letters_in_position[letter]) - answer.count(letter)) != 0

def refine_guess():
    global letters_in_position, combined_possibilities, non_letters
    letter_index = 0
    for letter in guess:
        if letter == answer[letter_index]:
            if letter in letters_in_position:
                letters_in_position[letter].append(letter_index) 
            else:
                letters_in_position[letter] = [letter_index]
            letter_index = letter_index + 1
        elif letter in answer:
            if letter in letters_in_position:
                letters_in_position[letter].append(letter_index) 
            else:
                letters_in_position[letter] = [letter_index]
            letter_index = letter_index + 1
        else:
            non_letters.append(letter)
            letter_index = letter_index + 1
    list1 = [i for i in letters_in_position.keys()]
    list2 = [i for i in letters_not_in_position.keys()]
    combined_possibilities = combined_possibilities + list1 + list2



def positional():
    global possible_words
    for word in possible_words["words"].copy():
        for key in letters_not_in_position:
            for value in letters_not_in_position[key]:
                if key == word[value]:
                    possible_words.discard(word)
                    break
    for word in possible_words.copy():
        for key in letters_in_position:
            for value in letters_in_position[key]:
                if key != word[value]:
                    possible_words["words"].discard(word)
                    break

def letters_known_word_refine():
    global possible_words
    for word in possible_words["words"].copy(): 
        for letter in combined_possibilities:
            if letter not in word:
                possible_words["words"].discard(word)   

def letters_remove_word_refine():
    global possible_words
    for word in possible_words["words"].copy():
        for letter in non_letters:
            if letter in word:
                possible_words["words"].discard(word)
                break

# need to remove words from possible words list - need to have a clear path of where posssible words is grabbing

def game_in_terminal():
    global letters_in_position, letters_not_in_position, combined_possibilities, non_letters
    # Dictonary for in game letters that are guessed - used to elimate possible words for optimal guess
    letters_in_position = {}
    letters_not_in_position = {}
    # List for all letters that are known in answer (from guess)
    combined_possibilities = []
    # anti-combined_possibilites -- could help when creating UI for the keyboard
    non_letters = []
    initial_refined_words()
    possible_words["words"] = set(all_words["words"])
    new_answer()
    call_guess_with_question()
    game_without_letters_filter()
    guess_number = 1
    while guess_number < 6 and guess != answer:
        guess_number = guess_number + 1
        refine_guess()
        positional()
        letters_known_word_refine()
        letters_remove_word_refine()

        ranking_refined_words()
        call_guess_without_question()
        game_without_letters_filter()
    if guess == answer:
        print(Fore.WHITE + f"Congratulations, you solved the puzzle in {guess_number} guesses!")
    else: 
        full_answer = "".join(answer)
        print(Fore.WHITE + f"So close... The answer was '{full_answer}'")
    

game_in_terminal()