#!/bin/python3:
import copy  # import the copy module to create deep copies of the path list
from collections import deque  # import deque from the collections module for efficient queue implementation

# define the word ladder function with start and end words, and optional dictionary file
def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    with open(dictionary_file, 'r') as f:
        words = [line.strip() for line in f]
    if end_word not in words:
        return None
    if start_word == end_word:
        return [start_word]
    ladder = deque([[start_word]])
    while ladder:
        path = ladder.popleft()
        last_word = path[-1]
        for word in words[:]:
            if word not in path and _adjacent(last_word, word):
                if word == end_word:
                    return path + [end_word]
                else:
                    ladder.append(copy.deepcopy(path) + [word])
                    words.remove(word)
    return None
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
