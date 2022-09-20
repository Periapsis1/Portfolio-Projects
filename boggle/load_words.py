
import json

FILE_NAME = 'words.json'

def load(file_name=FILE_NAME):
    filtered_words = {}
    words = {}

    with open(file_name, 'r') as f:
        words = json.load(f)

    for word in words.keys():
        if 2 < len(word) <= 16:  # no 2 letter words, and 16 letter words is the max
            filtered_words[word] = 1

    return filtered_words