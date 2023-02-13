#!/bin/python3:
import copy
from collections import deque


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


def verify_word_ladder(ladder):
    if len(ladder) == 1:
        return True
    if ladder is None or len(ladder) < 1:
        return False
    if len(ladder) < 2:
        return False
    for i in range(0, len(ladder) -1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    if len(word1) != len(word2):
        return False
    num_diff = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            num_diff += 1
            if num_diff > 1:
                return False
    return num_diff == 1
