#!/usr/bin/env python

from textblob import TextBlob
from sys import argv

FILENAME = argv[1]

with open(FILENAME, 'r') as f:
    text = TextBlob(f.read())
    print text.sentiment
