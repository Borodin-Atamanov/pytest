import random
import re
import string

fh = open('text-only.tsv','r').read()
unique_chars = set(fh)
len(unique_chars) #for the length.
print(unique_chars)

for char in sorted(unique_chars):
    print(char, end='')
