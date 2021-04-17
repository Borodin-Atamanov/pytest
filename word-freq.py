#!/usr/bin/env python3.9
# encoding=utf-8
import re
import json
import jsonpickle

#Debug function for printing complex data in human-readable format
def print_json (data):
    jsonpickle.set_preferred_backend('json')
    jsonpickle.set_encoder_options('json', ensure_ascii=False)
    json_str = jsonpickle.encode(data, unpicklable=False, fail_safe=None, indent=2, separators=(',', ':'))
    print (json_str)
    return json_str

f = open('input.csv', 'r')
text = str(f. readlines())
text = text.replace ('\\n', ' ')

#text = text[-3300:]
#print("%s\n" % text)
#print (text)

#words = re.findall('[^\s]', text) #Регулярка для слов от двух букв
#words = re.findall('[^\s]{2,}',text) #Регулярка для слов от двух букв
#words = re.findall('[a-zA-Z]{2,}',text) #Регулярка для слов от двух букв
#print("%s\n" % words)

#words = text.split(sep=r'\n ')
#words = text.split('[\s]')
#words = re.split(r'[\s\"\,\.\\\'\"\<\>\(\)\?\!\:\;\%\{\}\|\[\]\&\=\#]', text)
#words = re.split(r'[\s\"\,\.\\\'\"\<\>\(\)\?\!\:\;\%\{\}\|\[\]\&\=\#]', text)
words = re.split(r'[^a-zA-Z0-9А-Яа-яЁё_]', text)

#print (words)
words = sorted(words)
#exit()

words2 = []
for word in words:
    filtered_word = ''
    for char in word:
        if char not in "\n\r\t":
            filtered_word += char
    #words2[filtered_word] = {'count_stat': 1}
    filtered_word = filtered_word.lower()
    words2.append(filtered_word)

words = words2
#print_json (words)

stats = {}
for word in words:
    if len(word) > 1:
        stats[word] = stats.get(word, 0) + 1

#print_json (words)

stats = {k: v for k,v in sorted(stats.items(), reverse=True, key=lambda item: item[1]) }

#print_json (stats)
for word in stats:
    print ("\"{0}\",\"{1}\"".format(word, stats[word]))
#print(stats)

