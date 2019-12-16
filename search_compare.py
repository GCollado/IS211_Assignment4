#! usr/bin/env python
#! -*- coding: utf-8 -*-

"""
1. Create search_compare.py
2. Create four functions: sequential_search, ordered_sequential_search, binary_search_initiative,
and binary_search_recursive
3. Using Search and Binary search codes, modify each function to calculate how long it takes and
the results of the search function
4. Main function should print the average of each function;
    generate 100 random input lists containing positive numbers of size 500, 1000, and 1,000;
    worst-case scenario should contain do a search for a number not on the list
5.
"""
import timeit
from timeit import Timer
import random

#500, 1000, 10000

#should have a 100 list containing, 500, 1000, 1000
def sequential_search(number_list, number):
    position = 0
    found = False

    while position < len(number_list) and not found:
        if number_list[position] == number:
            found = True
        else:
            position = position + 1
    return found


def ordered_sequential_search(number_list, number):
    position = 0
    found = False
    stop = False

    while position < len(number_list) and not found and not stop:
        if number_list[position] == number:
            found = True
        elif number_list[position] > number:
            stop = True
        else:
            position = position + 1
    return found


def binary_search_iterative(number_list, number):
     first = 0
     last = len(number_list) -1
     found = False
     while first <= last and not found:
         midpoint = (first + last) //2
         if number_list[midpoint] == number:
             found = True
         elif number < number_list[midpoint]:
             last = midpoint -1
         else:
             first = midpoint + 1
     return found


def binary_search_recursive(number_list, number):
    if len(number_list) == 0:
        return False
    else:
        midpoint = len(number_list) //2
    if number_list[midpoint] == number:
        return True
    elif number < number_list[midpoint]:
        return binary_search_recursive(number_list[:midpoint], number)
    else:
        return binary_search_recursive(number_list[midpoint + 1:], number)

list_comp = [[x for x in range(1, 100)] for x in range(100)]

def  main():
    pass

ss = Timer("sequential_search(list_comp, 50)", "from __main__ import sequential_search")
oss = Timer("ordered_sequential_search(list_comp, 50)", "from __main__ import ordered_sequential_search")
bsi = Timer("binary_search_iterative(list_comp, 50)", "from __main__ import binary_search_iterative")
bsr = Timer("binary_search_recursive(list_comp, 50)", "from __main__ import binary_search_recursive")

#print('ss: ', ss.timeit(number=1000))
#print('oss: ', oss.timeit(number=1000))
#print('bsi: ', bsi.timeit(number=1000))
#print('bsr: ', bsr.timeit(number=1000))

#if __name__ == '__main__':
#    print(sequential_search(listcomp, 101))

i = 0
for listitem in list_comp:
    for item in listitem:
            if item  == 50:
                print('Number: 50', "list comp #:", list)


#print(sequential_search(list_comp, 50))