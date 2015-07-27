#!/usr/bin/env python

from __future__ import division, unicode_literals
import math
from textblob import TextBlob
from sys import argv

try:
    files = argv[1:]
except IndexError:
    print "Please provide at least one file. Exiting."
    exit(1)

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

bloblist = []
for f in files:
    print f
    blob = TextBlob(open(f, 'r').read())
    bloblist.append(blob)

for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:5]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
