from intervaltree import Interval, IntervalTree

#new IntervalTree

#Создаю интервальные деревья

#Объединяю интервалы


t1 = IntervalTree()
t2 = IntervalTree()
t1[10:20] = 'bsads'
t2[15:25] = 'dgsdf'

print(t1)
t3 = t1.union(t2)

#Соединяем интервалы
#t1 = IntervalTree()
t3.merge_overlaps()
#print(set(t3.items()))


for interval_obj in t3:
    print (interval_obj)


#for interval in t3: print (interval.begin, ' -- ', interval.end)
