from itertools import count
from operator import add, index
import numpy as np
import pandas as pd

def initalize():
    global words, list_of_lists, list_of_occur, list_of_duplicate_sorted, list_of_rank, list_of_rank_unique, possible_words, url
    global letter_in, letter_right, letter_one_score, possible_words_refined_scored, possible_words_refined_scored_ranked, word_score
    url = "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"
    words = pd.read_csv(url)
    list_of_lists = ["letter_one", "letter_two", "letter_three", "letter_four", "letter_five"]
    list_of_occur = ["letter_one_occur", "letter_two_occur", "letter_three_occur", "letter_four_occur", "letter_five_occur"]
    list_of_duplicate_sorted = ["letter_one_duplicate_sorted", "letter_two_duplicate_sorted", "letter_three_duplicate_sorted", "letter_four_duplicate_sorted", "letter_five_duplicate_sorted"]
    list_of_rank = ["letter_one_rank", "letter_two_rank", "letter_three_rank", "letter_four_rank", "letter_five_rank"]
    list_of_rank_unique = ["letter_one_rank_unique", "letter_two_rank_unique", "letter_three_rank_unique", "letter_four_rank_unique", "letter_five_rank_unique"]
    possible_words = set(words["lowes"])
    letter_in = ""
    letter_right = ""
    letter_one_score = []
    possible_words_refined_scored = []
    possible_words_refined_scored_ranked = []
    word_score = []

def create_letter_list():
    global letter_one, letter_two, letter_three, letter_four, letter_five
    letter_one = []
    letter_two = []
    letter_three = []
    letter_four = []
    letter_five = []

def letter_list():
    create_letter_list()
    for word in possible_words_refined:
        letter_index = 1
        for letter in word:
            if letter_index == 1:
                letter_one.append(letter)
                letter_index = letter_index + 1
            elif letter_index == 2:
                letter_two.append(letter)
                letter_index = letter_index + 1
            elif letter_index == 3:
                letter_three.append(letter)
                letter_index = letter_index + 1
            elif letter_index == 4:
                letter_four.append(letter)
                letter_index = letter_index + 1
            else:
                letter_five.append(letter)

def create_occurances_list():
    global letter_one_occur, letter_two_occur, letter_three_occur, letter_four_occur, letter_five_occur
    letter_one_occur = []
    letter_two_occur = []
    letter_three_occur = []
    letter_four_occur = []
    letter_five_occur = []

def occurances():
    create_occurances_list()
    list_index = 0
    for letter_list in list_of_lists:
        for letter in globals()[letter_list]:
                count = (globals()[letter_list]).count(f"{letter}")
                (globals()[list_of_occur[list_index]]).append(f"{count}.{letter}")
        list_index = list_index + 1

def create_ranking_sets_lists():
    global letter_one_duplicate_sorted, letter_one_rank, letter_one_rank_unique
    letter_one_duplicate_sorted = []
    letter_one_rank = []
    letter_one_rank_unique = []
    global letter_two_duplicate_sorted, letter_two_rank, letter_two_rank_unique
    letter_two_duplicate_sorted = []
    letter_two_rank = []
    letter_two_rank_unique = []
    global letter_three_duplicate_sorted, letter_three_rank, letter_three_rank_unique
    letter_three_duplicate_sorted = []
    letter_three_rank = []
    letter_three_rank_unique = []
    global letter_four_duplicate_sorted, letter_four_rank, letter_four_rank_unique
    letter_four_duplicate_sorted = []
    letter_four_rank = []
    letter_four_rank_unique = []
    global letter_five_duplicate_sorted, letter_five_rank, letter_five_rank_unique 
    letter_five_duplicate_sorted = []
    letter_five_rank = []
    letter_five_rank_unique = []

def get_rank(letter):
    rank = int(letter[:-2])
    return rank

def ranking_function():
    create_ranking_sets_lists()
    list_index = 0
    for list in list_of_duplicate_sorted:
        (globals()[list]) = sorted((globals()[list_of_occur[list_index]]), key= get_rank, reverse= True)
        for item in (globals()[list]):
            letter = item[len(item)-1:]
            (globals()[list_of_rank[list_index]]).append(letter)
        for value in (globals()[list_of_rank[list_index]]):
            if value not in (globals()[list_of_rank_unique[list_index]]):
                (globals()[list_of_rank_unique[list_index]]).append(value)
        list_index = list_index + 1

def get_letters_and_ranks():
    letter_list()
    occurances()
    ranking_function()

def correct_letter(): 
    global letters_in_position, letter_right
    letter_right = input("Which letter? ")
    if letter_right not in letters_in_position.keys():       
        letters_in_position[f"{letter_right}"] = [int(guess.index(letter_right))]
    else:
        index_pos = len(guess) - guess[::-1].index(letter_right) - 1
        letters_in_position[f"{letter_right}"].append(int(index_pos))
    
def in_word_letter():
    global letters_not_in_position, letter_in
    letter_in = input("Which letter? ")
    if letter_in not in letters_not_in_position.keys():
        letters_not_in_position[f"{letter_in}"] = [int(guess.index(letter_in))]
    else:
        letters_not_in_position[f"{letter_in}"].append(int(guess.index(f"{letter_in}")))

def positional():
    global possible_words_refined
    for word in possible_words_refined.copy():
        for key in letters_not_in_position:
            for value in letters_not_in_position[key]:
                if key == word[value]:
                    possible_words_refined.discard(word)
                    break
    for word in possible_words_refined.copy():
        for key in letters_in_position:
            for value in letters_in_position[key]:
                if key != word[value]:
                    possible_words_refined.discard(word)
                    break

def letters_known_word_refine():
    global possible_words_refined
    for word in possible_words_refined.copy(): 
        for letter in combined_possibilities:
            if letter not in word:
                possible_words_refined.discard(word)   

def letters_remove_word_refine():
    global possible_words_refined
    for word in possible_words_refined.copy():
        for letter in non_letters:
            if letter in word:
                possible_words_refined.discard(word)
                break

def make_a_guess():
    global guess, non_letters, letters_in_position, letters_not_in_position, possible_words_refined, list1, list2, combined_possibilities
    ending_criteria = ""   
    while ending_criteria != 'y':
        guess = input("What word did you guess? ")
        guess = [*guess]
        initial_correct = input("Were there any correctly positioned letters? y/n ")
        while initial_correct == 'y':
            correct_letter()
            initial_correct = input("Anymore? y/n ")
        second_correct = input("Were there any correctly guessed letters? y/n ")
        while second_correct == 'y':
            in_word_letter()
            second_correct = input("Anymore? y/n ")
        list1 = [i for i in letters_in_position.keys()]
        list2 = [i for i in letters_not_in_position.keys()]
        combined_possibilities = combined_possibilities + list1 + list2
        for letter in guess:
            if letter not in combined_possibilities:
                non_letters.append(letter)
        possible_words_refined = possible_words.copy()
        positional()
        letters_known_word_refine()
        letters_remove_word_refine()
        get_letters_and_ranks()
        ranking_initial()
        ending_criteria = input("Game over? y/n ")

def get_rank_word(word):
    rank = int(word[:-6])
    return rank

def ranking_initial():
    global possible_words_refined_scored, possible_words_refined_scored_ranked, word_score
    possible_words_refined_scored = []
    possible_words_refined_scored_ranked = []
    for word in possible_words_refined:
        word_score = []
        letter_index = 0
        for letter in word:
            if letter_index < 4:
                # Get frequency of letter in the position of word
                position = (globals()[list_of_lists[letter_index]]).index(letter)
                letter_score = int(globals()[list_of_duplicate_sorted[letter_index]][position][:-2])
                word_score.append(letter_score)
                letter_index = letter_index + 1
            else:
                position = (globals()[list_of_lists[letter_index]]).index(letter)
                letter_score = int(globals()[list_of_duplicate_sorted[letter_index]][position][:-2])
                word_score.append(letter_score)
                letter_index = letter_index + 1
                total_score = sum(word_score)   
                possible_words_refined_scored.append(f"{total_score}.{word}")
    possible_words_refined_scored = sorted(possible_words_refined_scored, key= get_rank_word)
    for word in possible_words_refined_scored:
        possible_words_refined_scored_ranked.append(word[len(word)-5:])
    total_words = len(possible_words_refined_scored_ranked)
    print(f"Total words left: {total_words}")
    if total_words < 5:
        print(possible_words_refined_scored_ranked)
    else:
        print(f"{possible_words_refined_scored_ranked[0]}\n{possible_words_refined_scored_ranked[1]}\n{possible_words_refined_scored_ranked[2]}")
        print(f"{possible_words_refined_scored_ranked[3]}\n{possible_words_refined_scored_ranked[4]}")

# score each and add it to the word then use rank function to sort words
# function for word that doesn't include perfect letters and looks only at frequency    
    print("done")

def new_game():
    global list1, list2, combined_possibilities, guess, non_letters, letters_not_in_position, letters_in_position, possible_words_refined, possible_words
    initalize()
    list1 = []
    list2 =[]
    possible_words_refined = set()
    combined_possibilities = []
    letters_in_position = {}
    letters_not_in_position = {}
    non_letters = []
    guess = []
    possible_words_refined = possible_words.copy()
    get_letters_and_ranks()
    ranking_initial()
    make_a_guess()
