import re
import re

inp = 'Привет\n\rКак дела?'
filter = "\n\r\t "

#w = w.maketrans(' ', ' ', "\n\r\t")
#w = w.translate(None, ",!.;\n")
#print (w)

s = "asjo,fdjk;djaso,oio!kod.kjods;dkps"
#s = s.translate(None, ",!.;")
#s = s.translate(dict.fromkeys(map(ord, u"\n,!.;")))
#w = w.translate(dict.fromkeys(map(ord, u"\n,!.;")))
#w = w.translate(string.maketrans('', ''), '!@#$')
#w = w.translate(str.maketrans('', '', "!@#$?\n"))
#w = w.replace('\n', "")
outp = '';
for char in inp:
    if char not in filter:
        outp += char



#print (s)

print (outp)
exit ()

mystring = """
Все посчита{л|ла}? Сначала скажиме мне, сколько квадратов ты наш{ел|ла} в этой фигуре?
"""
print (mystring)
pos = {}
pos[0] = mystring.find("{")
pos[1] = mystring.find("|")
pos[2] = mystring.find("}")
print (pos)
exit()

#pattern = re.compile(r'(\{.*?\})', re.DOTALL)
pattern = re.compile(r'(\s*)', re.DOTALL)
newstring = pattern.sub(r"\1", mystring, "_ЗАМЕНА_")
#newstring = re.sub(pattern, r"\1", '_!_')




regex = r'\#\s*\#';
regul = re.compile(regex, re.DOTALL)

new = 'Какая-то ######строка #### #######  # # тут нет тегов #'
new = """
Все посчита{л|ла}? Сначала скажиме мне, сколько квадратов ты наш{ел|ла} в этой фигуре?
"""
print (new)
#new = re.sub(r'\#\s*\#', '#', new)
#new = re.sub(r'\# \#', '##', new) #works!
#new = re.sub(r'\#\s{1,}\#', '##', new) #works
#finder_str = ''+s+r'[\s\r\n]{1,}'+s+''
print (f" [[[ {finder_str} ]]]")
new = re.sub(finder_str, '##', new) #works
print (new)



exit()

for i in range (0, 6):
    new = re.sub(r'\#\s\s\s\s\#', '##', new)
    print (new)
    new = re.sub(r'\#\s\s\s\#', '##', new)
    print (new)
    new = re.sub(r'\#\s\s\#', '##', new)
    print (new)
    new = re.sub(r'\#\s\#', '##', new)
    print (new)
#new = re.sub(r'\#\s+\#', '##', new) #works!


