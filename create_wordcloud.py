#!/usr/bin/env python

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sys import argv

try:
    filename = argv[1]
except:
    print "Please provide a filename argument. Exiting."
    exit(1)

text = open(filename).read().decode('utf8')
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
