#!/usr/bin/env python

import shelve

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
    filename = person[0] + '.txt'
    # Write all messages by same person to same text file, accounting for nicknames.
    for key in person:
        messages = [tup[0] for tup in my_dict[key]]
        with open(filename, 'a') as f:
            f.write(str(messages)[1:-1])

shelf_dict.close()
