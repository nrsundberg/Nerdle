import csv
possible_words = {'word' : []}

words = []
possible_words = []
with open('words_dictonary.csv', 'r') as read_obj:
    read = csv.reader(read_obj)
    words = list(read)
for lists in words:
    for word in lists:
        possible_words['word'].append(word)


def ranking_every_word():
    global word_score, all_words_scored_ranked, all_words_scored, total_words
    total_words = int()
    all_words_scored_ranked = []
    all_words_scored = []
    for word in possible_words:
        word_score = []
        letter_index = 0
        for letter in word:
            if letter_index < 4:
                # Get frequency of letter in the position of word
                position = (globals()[list_of_lists[letter_index]]).index(letter)
                letter_score = int(globals()[list_of_occur[letter_index]][position][:-2])
                word_score.append(letter_score)
                letter_index = letter_index + 1
            else:
                position = (globals()[list_of_lists[letter_index]]).index(letter)
                letter_score = int(globals()[list_of_occur[letter_index]][position][:-2])
                word_score.append(letter_score)
                letter_index = letter_index + 1
                total_score = sum(word_score)   
                all_words_scored.append(f"{total_score}.{word}")
    all_words_scored = sorted(all_words_scored, key= get_rank_word, reverse= True)
    for word in all_words_scored:
        all_words_scored_ranked.append(word[len(word)-5:])
    total_words = len(all_words_scored_ranked)
