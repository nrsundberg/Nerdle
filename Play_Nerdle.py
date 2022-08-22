from random import sample
import V_one
import csv

V_one.open_functionality()

with open('answers.csv', 'r') as read_obj:
        read = csv.reader(read_obj)
        import_answers = list(read)
for lists in import_answers:
    for word in lists:
        possible_answers.append(word)

def new_answer():
    global answer, answer_letters
    answer_letters = []
    answer = sample(possible_answers , k= 1)
    for word in answer:
        for letter in word:
            answer_letters.append(letter)

# var to init on open
possible_words_dict = {}
possible_words_dict['words'] = V_one.possible_words
letters_in_position = {}
letters_in_word = {}
color_list = [V_one.Fore.WHITE, V_one.Fore.WHITE, V_one.Fore.WHITE, V_one.Fore.WHITE, V_one.Fore.WHITE]
import_answers = []    
possible_answers = []

def correct_letter():
    global letters_in_position, letter_right
    letter_right = input("Which letter? ")
    if letter_right not in letters_in_position.keys():       
        letters_in_position[f"{letter_right}"] = [int(guess.index(letter_right))]
    else:
        index_pos = len(guess) - guess[::-1].index(letter_right) - 1
        letters_in_position[f"{letter_right}"].append(int(index_pos))


def play_in_term_game():
    global guess, possible_words_dict, answer
    new_answer()
    guess = []
    guess = input("Please guess a word ")
    while guess not in possible_words_dict['words']:
        guess = input(V_one.Fore.RED + "Please guess a valid 5-letter word ")
    guess = [*guess]
    letter_index = 0
    for letter in guess:
        if letter == answer_letters[letter_index]:
            color_list[letter_index] = V_one.Fore.GREEN
            letter_index += 1
        elif letter in answer_letters:
            color_list[letter_index] = V_one.Fore.YELLOW
            letter_index += 1
        else:
            color_list[letter_index] = V_one.Fore.BLACK
            letter_index += 1
    print(color_list[0] + guess[0] + color_list[1] + guess[1] + color_list[2] + guess[2] + color_list[3] + guess[3] + color_list[4] + guess[4])


