#!/usr/bin/env python

from sys import argv
from sentence_generator import buildMapping, wordlist, genSentence

try:
    FILENAME = argv[1]
    CHAIN_LENGTH = int(argv[2])
    NUM_TIMES = int(argv[3])
except IndexError:
    print "Please provide filename, chain length, and number of times to run. Exiting."
    exit(1)

if CHAIN_LENGTH < 2: 
    print "Markov chain length must be at least 2. Exiting."
    exit(1)

buildMapping(wordlist(FILENAME), CHAIN_LENGTH)

print genSentence(CHAIN_LENGTH + 1)
for i in xrange(NUM_TIMES - 2):
    print genSentence(CHAIN_LENGTH)
print genSentence(CHAIN_LENGTH - 1)
