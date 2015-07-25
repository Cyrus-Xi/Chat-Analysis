#!/usr/bin/env python

from textblob import TextBlob
from sys import argv
import operator
from pprint import pprint
from nltk.corpus import stopwords

try:
    filename = argv[1]
except:
    print "Please specify a filename. Exiting."
    exit(1)

transcript = open(filename, 'r').read().encode('utf8')

stop = stopwords.words('english')
transcript_stop = str([word for word in transcript.split() if word not in stop])
#transcript_stop_3 = str([word for word in transcript_stop.split() if len(word) > 2])
blob = TextBlob(transcript_stop)
#blob3 = TextBlob(transcript_stop_3)

# Sorted list representation of the dict.
sorted_word_counts = sorted(blob.word_counts.items(), key=operator.itemgetter(1), reverse=True)
sorted_word_counts = [(word, freq, len(word)) for (word, freq) in sorted_word_counts]

NUM_WORDS = 30
pprint(sorted_word_counts[:NUM_WORDS])

total = 0
for tup in sorted_word_counts[:NUM_WORDS]:
    total += tup[2]

avg = float(total) / NUM_WORDS
print avg
