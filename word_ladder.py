#!/bin/python3:
import copy  # import the copy module to create deep copies of the path list
from collections import deque  # import deque from the collections module for efficient queue implementation

# define the word ladder function with start and end words, and optional dictionary file
def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    with open(dictionary_file, 'r') as f:  # open the dictionary file in read mode
        words = [line.strip() for line in f]  # read each line and strip trailing whitespace
    if end_word not in words:  # check if the end word is in the list of words
        return None  # if not, return None
    if start_word == end_word:  # check if the start word is the same as the end word
        return [start_word]  # if so, return a list with the start word as the only element
    ladder = deque([[start_word]])  # create a deque containing a list with the start word as the only element
    while ladder:  # loop until the ladder is empty
        path = ladder.popleft()  # get the next path from the ladder
        last_word = path[-1]  # get the last word in the path
        for word in words:  # loop through the remaining words in the dictionary
            if word not in path and _adjacent(last_word, word):  # check if the word is adjacent to the last word in the path and not already in the path
                if word == end_word:  # if the word is the end word, return the path plus the end word
                    return path + [end_word]
                else:  # otherwise, add a new path with the word appended to the end to the ladder
                    ladder.append(copy.deepcopy(path) + [word])  # create a deep copy of the path list and append the new word to it
                    words.remove(word)  # remove the word from the list of remaining words in the dictionary to prevent cycles in the ladder
    return None  # if the ladder is empty and the end word has not been found, return None

# define the verify word ladder function to check if a word ladder is valid
def verify_word_ladder(ladder):
    if len(ladder) == 1:
        return True
    if ladder is None or len(ladder) < 1:
        return False
    if len(ladder) < 2:  # check if the ladder has at least two words
        return False  # if not, return False
    for i in range(0, len(ladder)-1):  # loop through the ladder, starting at the second word
        if not _adjacent(ladder[i], ladder[i+1]):  # check if each adjacent pair of words in the ladder is adjacent
            return False  # if not, return False
    return True  # if all adjacent pairs of words are adjacent, return True

# define the adjacent function to check if two words are adjacent
def _adjacent(word1, word2):
    if len(word1) != len(word2):  # check if the words are the same length
        return False  # if not, they can't be adjacent

    num_diff = 0  # initialize a counter for the number of differing characters
    for i in range(len(word1)):  # loop through the characters in the words
        if word1[i] != word2[i]:  # if the characters differ
            num_diff += 1  # increment the difference counter
            if num_diff > 1:  # if there is more than one difference, the words can't be adjacent
                return False
    return num_diff == 1 
