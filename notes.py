# V_one misc
try_one = ["letter_one_duplicate_sorted", "letter_two_duplicate_sorted", "letter_three_duplicate_sorted", "letter_four_duplicate_sorted", "letter_five_duplicate_sorted"]
try_two = ["letter_one_rank", "letter_two_rank", "letter_three_rank", "letter_four_rank", "letter_five_rank"]

item_index = 0
for item in try_two:
    index_letter_now = globals()[try_two[item_index]].index('s')
    value = globals()[try_one[item_index]][index_letter_now]
    print(value)
    item_index = item_index + 1

all_letters = []
for word in possible_words:
    for letter in word:
        all_letters.append(letter)

list_of_letters = set(all_letters)
list_of_letters = list(list_of_letters)
# Find absolute frequency of letters in any position
list_of_letters_scored = []
for letter in list_of_letters:
    count_letter = all_letters.count(letter)
    list_of_letters_scored.append(f"{count_letter}.{letter}")
sorted(list_of_letters_scored, key=get_rank, reverse= True)[:5]
# Find relative frequency of letters in any position
list_of_letters_scored = []
for letter in list_of_letters:
    count_letter = float(all_letters.count(letter))
    rel_freq = round(count_letter / float(len(possible_words)), ndigits=3)
    list_of_letters_scored.append(f"{rel_freq}.{letter}")
sorted(list_of_letters_scored, key=get_rank, reverse= True)[:5]

all_words_scored_ranked.index('crane')