#!/usr/bin/env python

import shelve
import re
from sys import argv
from nltk.corpus import stopwords

try:
    option = argv[1]
    filename_suffix = argv[2]
except IndexError:
    filename_suffix = ''

shelf_dict = shelve.open('my_shelf')
try:
    my_dict = shelf_dict['my_dict']
except:
    print "There's no dict in memory, exiting."
    exit(1)

# Get names programmatically-ish.
with open('dict_names.txt', 'r') as f:
    names = f.read().splitlines()

# The format looks something like this:
# A_name | A_nickname
# B_name | B_altname | B_nickname
name_poss = [(p.split('|')[0][:-1], p.split('|')[1][1:-1], p.split('|')[2][1:]) 
            if p.count('|') == 2 else (p.split('|')[0][:-1], p.split('|')[1][1:]) 
            if '|' in p else [p] for p in names]

for person in name_poss:
    if not filename_suffix: filename = person[0] + '.txt'
    else: filename = person[0] + filename_suffix + '.txt'
    # Write all messages by same person to same text file, accounting for nicknames.
    for key in person:
        messages = [tup[0] for tup in my_dict[key]]
        messages = str(messages).replace("'", "").replace('"', '')[1:-1]
        # Take out unparseable unicode (e.g., \xe0).
        msgs = re.sub(r'\\x..', '', messages) 
        if option == 'stop':
            stop = stopwords.words('english')
            msgs_stop = [word for word in msgs.split() if word not in stop]
            msgs = ' '.join(msgs_stop)
        elif option == 'newline':
            msgs = '\n'.join(msgs.split(', '))
        elif option == 'space':
            msgs = ' '.join(msgs.split(', '))
        elif option == 'period':
            msgs = '. '.join(msgs.split(', '))
        with open(filename, 'a') as f:
            f.write(msgs.encode('utf8'))

shelf_dict.close()
