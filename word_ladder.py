#!/bin/python3:
import copy  # import the copy module to create deep copies of the path list
from collections import deque  # import deque from the collections module for efficient queue implementation

# define the word ladder function with start and end words, and optional dictionary file
def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    with open(dictionary_file, 'r') as f:
        words = [line.strip() for line in f]  # read in the dictionary file and strip whitespace from each line
    if end_word not in words:
        return None  # if the end word is not in the dictionary, there can be no word ladder
    if start_word == end_word:
        return [start_word]  # if the start and end words are the same, the ladder is just that one word
    ladder = deque([[start_word]])  # create a deque with a list containing the start word
    while ladder:  # loop until the deque is empty (i.e., all possible ladders have been checked)
        path = ladder.popleft()  # take the leftmost path from the deque
        last_word = path[-1]  # get the last word in the path
        for word in words[:]:  # loop through a copy of the word list (so we can modify the original list without affecting the loop)
            if word not in path and _adjacent(last_word, word):  # if the word is not already in the path and is adjacent to the last word in the path
                if word == end_word:  # if the word is the end word, the ladder is complete
                    return path + [end_word]  # return the ladder (the current path plus the end word)
                else:  # if the word is not the end word, add it to the path and append the new path to the deque
                    ladder.append(copy.deepcopy(path) + [word])
                    words.remove(word)  # remove the word from the word list (so we don't check it again in subsequent loops)
    return None  # if we have checked all possible paths and not found a ladder, return None
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
