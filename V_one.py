from cgi import test
from glob import glob
from itertools import count
from math import comb
from operator import add, index
from timeit import repeat
from turtle import pos, position
import numpy as np
import pandas as pd

url = "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"
words = pd.read_csv(url)
list_of_lists = ["letter_one", "letter_two", "letter_three", "letter_four", "letter_five"]
list_of_occur = ["letter_one_occur", "letter_two_occur", "letter_three_occur", "letter_four_occur", "letter_five_occur"]
list_of_duplicate_sorted = ["letter_one_duplicate_sorted", "letter_two_duplicate_sorted", "letter_three_duplicate_sorted", "letter_four_duplicate_sorted", "letter_five_duplicate_sorted"]
list_of_rank = ["letter_one_rank", "letter_two_rank", "letter_three_rank", "letter_four_rank", "letter_five_rank"]
list_of_rank_unique = ["letter_one_rank_unique", "letter_two_rank_unique", "letter_three_rank_unique", "letter_four_rank_unique", "letter_five_rank_unique"]
possible_words = words["lowes"].tolist()

def create_letter_list():
    global letter_one
    global letter_two
    global letter_three
    global letter_four
    global letter_five
    letter_one = []
    letter_two = []
    letter_three = []
    letter_four = []
    letter_five = []

def letter_list():
    create_letter_list()
    for word in words['lowes']:
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
    global letter_one_occur
    global letter_two_occur
    global letter_three_occur
    global letter_four_occur
    global letter_five_occur
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
    global letter_one_duplicate_sorted
    letter_one_duplicate_sorted = []
    global letter_one_rank
    letter_one_rank = []
    global letter_one_rank_unique  
    letter_one_rank_unique = []
    global letter_two_duplicate_sorted
    letter_two_duplicate_sorted = []
    global letter_two_rank
    letter_two_rank = []
    global letter_two_rank_unique  
    letter_two_rank_unique = []
    global letter_three_duplicate_sorted
    letter_three_duplicate_sorted = []
    global letter_three_rank
    letter_three_rank = []
    global letter_three_rank_unique  
    letter_three_rank_unique = []
    global letter_four_duplicate_sorted
    letter_four_duplicate_sorted = []
    global letter_four_rank
    letter_four_rank = []
    global letter_four_rank_unique  
    letter_four_rank_unique = []
    global letter_five_duplicate_sorted
    letter_five_duplicate_sorted = []
    global letter_five_rank
    letter_five_rank = []
    global letter_five_rank_unique  
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
    return "done"

def correct_letter(): 
    global letters_in_position
    letter_right = input("Which letter? ")
    if letter_right not in letters_in_position.keys():       
        letters_in_position[f"{letter_right}"] = int(guess.index(letter_right))
    else:
        letters_in_position[f"{letter_right}"].append(int(guess.index(letter_right)))

def in_word_letter():
    global letters_not_in_position
    letter_in = input("Which letter? ")
    if letter_in not in letters_not_in_position.keys():
        letters_not_in_position[f"{letter_in}"] = int(guess.index(letter_in))
    else:    
        letters_not_in_position[f"{letter_in}"].append(int(guess.index(f"{letter_in}")))

def positional():
    global possible_words_refined
    for word in possible_words_refined.copy():
        for key in letters_not_in_position:
            if key == word[letters_not_in_position[key]]:
                possible_words_refined.remove(word)
                break
    for word in possible_words_refined.copy():
        for key in letters_in_position:
            if key != word[letters_in_position[key]]:
                possible_words_refined.remove(word)
                break

def letters_known_word_refine():
    global possible_words_refined
    letters_known = len(combined_possibilities) - 1
    for word in possible_words:
        letter_index = 0 
        for letter in combined_possibilities:
            if letter in word and letter_index < letters_known:
                letter_index = letter_index + 1
            elif letter in word and letter_index == letters_known:
                possible_words_refined.append(word)   
            else:
                break

def letters_known_word_refine_two():
    global possible_words_refined
    for word in possible_words: 
        for letter in combined_possibilities:
            if letter not in word:
                possible_words_refined.remove(word)   

def letters_remove_word_refine():
    global possible_words_refined
    for word in possible_words_refined.copy():
        for letter in non_letters:
            if letter in word:
                possible_words_refined.remove(word)
                break

def make_a_guess():
    global guess, non_letters, letters_in_position, letters_not_in_position, possible_words_refined, list1, list2, combined_possibilities   
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
    possible_words_refined = possible_words
    positional()
    letters_known_word_refine_two()
    letters_remove_word_refine()
    print(possible_words_refined)

def new_game():
    global list1, list2, combined_possibilities, guess, non_letters, letters_not_in_position, letters_in_position, possible_words_refined
    list1 = []
    list2 =[]
    possible_words_refined = []
    combined_possibilities = []
    letters_in_position = {}
    letters_not_in_position = {}
    non_letters = []
    guess = []
    make_a_guess()

# need to do double letter