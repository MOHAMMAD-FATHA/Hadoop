#!/usr/bin/env python

import sys

current_word = None
word_len = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    word,length = line.split('\t')

    
    
    if current_word == word:
        word_len == length
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, word_len))
        word_len = length
        current_word = word
# for printing the last word
if current_word == word:
    print('%s\t%s' % (current_word, word_len))
