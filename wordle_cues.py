#===============================================================================================
# Script for returning a list of possible plays for the popular word-game Wordle
# Date: 11.03.2022
# Author: Tobias Fritz
# Summary:
# Requires an initial guess that provides a set of rules for the wordlist
#===============================================================================================

from nltk.corpus import words

#===============================================================================================

# list of letters (str) that are not part of the word
exclusion_list = []
# list of letters (str) that are part of the word
contained_list = []
# dictionary of known positions of letters (int:str)
position_dict = {}
# dictionary of known not-positions of letters (int:str)
position_dict_rev = {}

word_list = [ ]
for word in words.words():
    if len(word) == 5:
        word_list.append(word)

def check_dict(word_list, key, value):
    shortlist = []
    for i in word_list:
        if i[key] == value:
            shortlist.append(i)
    return shortlist

def check_dict_rev(word_list, key, value):
    shortlist = []
    for i in word_list:
        if i[key] != value:
            shortlist.append(i)
    return shortlist

def update_word_list(exclusion_list= exclusion_list, contained_list = contained_list, position_dict= position_dict,position_dict_rev = position_dict_rev, word_list= word_list):
    new_word_list= []
    for word in word_list:
        if exclusion_list and contained_list: 
            if not any(x in word for x in exclusion_list):
                if all(x in word for x in contained_list):
                    new_word_list.append(word)
        elif exclusion_list and not contained_list:
            if not any(x in word for x in exclusion_list):
                new_word_list.append(word)

        elif not exclusion_list and contained_list:
            if all(x in word for x in contained_list):
                new_word_list.append(word)

    if position_dict:
        for key, value in position_dict.items():
            new_word_list   = check_dict(word_list = new_word_list, key = key-1 , value = value)
        

    if position_dict_rev:
        for key, value in position_dict_rev.items():
            new_word_list   = check_dict_rev(word_list = new_word_list, key = key-1 , value = value)
                
        
    return new_word_list

    # update for dist dictionary

word_list = update_word_list()
print(word_list)
