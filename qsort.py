#!/usr/bin/python

qsort = lambda l : l if len(l)<=1 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort([x for x in l[1:] if x >= l[0]])
print(qsort([1,2,5,7,8,2,6,8,13,11,88,45,12]))
