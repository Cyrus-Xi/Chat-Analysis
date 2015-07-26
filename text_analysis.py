#!/usr/bin/env python

from textblob import TextBlob
from sys import argv
import operator
from pprint import pprint
from nltk.corpus import stopwords

try:
    FILENAME = argv[1]
    NUM_WORDS = int(argv[2])
except:
    print "Please specify a filename and number of words to return.. Exiting."
    exit(1)

transcript = open(FILENAME, 'r').read()

stop = stopwords.words('english')
transcript_stop = str([word for word in transcript.split() if word not in stop])
blob = TextBlob(transcript_stop)

# Sorted list representation of the dict.
sorted_word_counts = sorted(blob.word_counts.items(), key=operator.itemgetter(1), reverse=True)
sorted_word_counts = [(word.encode('utf8'), freq) for (word, freq) in sorted_word_counts]
sorted_word_counts_len = [(word, freq, len(word)) for (word, freq) in sorted_word_counts]

pprint(sorted_word_counts[:NUM_WORDS])

total = 0
for tup in sorted_word_counts_len[:NUM_WORDS]:
    total += tup[2]

avg = round((float(total) / NUM_WORDS), 2)
print "\nAverage length of your " + str(NUM_WORDS) + " most frequent words: " + str(avg) + "."
