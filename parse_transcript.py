#!/usr/bin/env python

from bs4 import BeautifulSoup, SoupStrainer
from re import compile, sub
from collections import defaultdict
from sys import argv
import shelve
from pprint import pprint

# Load pre-existing dict if possible.
shelf_dict = shelve.open('my_shelf')

# Only parse relevant HTML.
only_blocks = SoupStrainer('div', class_ = 'messageBlock')

# lxml is more performant than built-in parser.
soup = BeautifulSoup(open(argv[1]), 'lxml', parse_only = only_blocks)

# Get all divs that belong to the messageBlock class.
message_blocks = soup.find_all('div', class_ = 'messageBlock')

# If didn't load dict from shelf.
if not shelf_dict: SHELF_EXISTED = False
else: SHELF_EXISTED = True

# If key not in dict, don't throw KeyError and initialize with an empty list value.
master_dict = defaultdict(list)

for block in message_blocks:
    # Ignore system messages.
    if not block['timestamp']: continue
    # Unix-style timestamp.
    timestamp = int(block['timestamp'])
    # Get all the titles from the other* divs, including otherCont*.
    title = block.find('div', class_ = compile('other'))['title']
    # Get and remove time from title (e.g., title="Xi, Cyrus [9:42:54 AM]").
    time_pattern = compile(r'\[.+\]')
    time = time_pattern.search(title).group()[1:-1]
    # The name is what's left.
    name = time_pattern.sub('', title)[:-1]
    # Get the text from all message* (including messageCont*) divs.
    message = block.find('div', class_ = compile('message')).get_text()[:-1]
    message = message.encode('utf-8')
    # Store both time and timestamp, because timestamps are unique and can order.
    master_val_tup = (message, time, timestamp)
    master_dict[name].append(master_val_tup)

master_dict = dict(master_dict)

# If had pre-existing dict, merge the two dicts.
if SHELF_EXISTED:
    keys = set(shelf_dict['my_dict']).union(master_dict)
    no = []
    # Generator expression.
    # Make use of d.get(k, default) functionality.
    master_dict = dict((k, shelf_dict['my_dict'].get(k, no) + master_dict.get(k, no)) for k in keys)
        
# Pretty print.
pprint(master_dict)

# Update shelf.
shelf_dict['my_dict'] = master_dict
shelf_dict.close()
