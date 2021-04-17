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

def bigramEstimation(file):
    '''A very basic solution for the sake of illustration.
       It can be calculated in a more sophesticated way.
       '''

    lst = [] # This will contain the tokens
    unigrams = {} # for unigrams and their counts
    bigrams = {} # for bigrams and their counts

    # 1. Read the textfile, split it into a list
    text = open(file, 'r').read()
    #lst = text.strip().split()
    lst = re.split(r'[^a-zA-Z0-9А-Яа-яЁё_]', text)
    print ('Read ', len(lst), ' tokens...')
    #print_json (lst)

    del text # No further need for text var



    # 2. Generate unigrams frequencies
    for l in lst:
        if not l in unigrams:
            unigrams[l] = 1
        else:
            unigrams[l] += 1

    print ('Generated ', len(unigrams), ' unigrams...')

    # 3. Generate bigrams with frequencies
    for i in range(len(lst) - 1):
        temp = (lst[i], lst[i+1]) # Tuples are easier to reuse than nested lists
        if not temp in bigrams:
            bigrams[temp] = 1
        else:
            bigrams[temp] += 1

    print ('Generated ', len(bigrams), ' bigrams...')

    # Now Hidden Markov Model
    # bigramProb = (Count(bigram) / Count(first_word)) + (Count(first_word)/ total_words_in_corpus)
    # A few things we need to keep in mind
    total_corpus = sum(unigrams.values())
    # You can add smoothed estimation if you want


    print ('Calculating bigram probabilities and saving to file...')

    # Comment the following 4 lines if you do not want the header in the file.
    with open("bigrams.txt", 'w') as out:
        out.write('Bigram' + '\t' + 'Bigram Count' + '\t' + 'Uni Count' + '\t' + 'Bigram Prob')
        out.write('\n')
        out.close()


    for k,v in bigrams.items():
        # first_word = helle in ('hello', 'world')
        first_word = k[0]
        first_word_count = unigrams[first_word]
        bi_prob = bigrams[k] / unigrams[first_word]
        uni_prob = unigrams[first_word] / total_corpus

        final_prob = bi_prob + uni_prob
        with open("bigrams.txt", 'a') as out:
            out.write(k[0] + ' ' + k[1] + '\t' + str(v) + '\t' + str(first_word_count) + '\t' + str(final_prob)) # Delete whatever you don't want to print into a file
            out.write('\n')
            out.close()




# Callings
bigramEstimation('input.csv')

exit()

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

