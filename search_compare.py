#! usr/bin/env python
#! -*- coding: utf-8 -*-


"""
====================================
Part 1 - Search Algorithm Comparison
====================================
1. Create a 'search_compare.py' file.
2. Create 4 functions using the codes from the 'Sequential and Binary Search'
 section:
    a. sequential_search
    b. ordered_sequential_search
    c. binary_search_iterative
    d. binary_search_recursive
3. Modify each code to calculate the time required to return the results
4. The program's main function is to return how long the function takes to
 return the results on average. Generate 100 random positive integer input lists
 of size 500, 1000, and 10000. Find the average run time of the 100 lists.
    a. Generate 100 lists each list set containing 500, 100, and 10000.
    b. Using worst-case scenario, search for an element we know that will not be
     in the list. Use -1 to search.
    c. The results should display: 'Sequential Search Took % 10.7f seconds to run
     on average.'
    d. The binary and ordered sequential search functions the lists should be
    sorted before searching.
"""

import random
import timeit


def sequential_search(search_number, size):
    lists_of_numbers = [[random.randint(1,100) for number in range(100)] for number_list in range(size)]
    position = 0
    found = False
    for number_list in lists_of_numbers:
        while search_number < len(number_list) and not found:
            if number_list[position] == search_number:
                found = True
            else:
                position += 1
        return found


def ordered_sequential_search(search_number, size):
    lists_of_numbers = [[random.randint(1, 100) for number in range(100)] for number_list in range(size)]
    position = 0
    found = False
    for number_list in lists_of_numbers:
        number_list = sorted(number_list)
        while position < len(number_list) and not found:
            if number_list[position] == search_number:
                found = True
            else:
                position += 1
    return found


def binary_search_iterative(search_number, size):
    lists_of_numbers = [[random.randint(1, 100) for number in range(100)] for number_list in range(size)]
    found = False
    for number_list in lists_of_numbers:
        first_number, last_number = 0, len(number_list) - 1
        number_list = sorted(number_list)
        while first_number <= last_number and not found:
            middle = (first_number + last_number)//2
            if number_list[middle] == search_number:
                found = True
            elif search_number < number_list[middle]:
                last_number = middle - 1
            else:
                first_number = middle + 1
        return found


def binary_search_recursive(search_number, size):
    lists_of_numbers = [[random.randint(1, 100) for number in range(100)] for number_list in range(size)]
    for number_list in lists_of_numbers:
        number_list = sorted(number_list)
        if len(number_list) == 0:
            return False
        else:
            middle = len(number_lists)//2
        if number_list[middle] == search_number:
            return True
        elif search_number < number_list[middle]:
            return binary_search_recursive(search_number, number_list[:middle])
        else:
            return binary_search_recursive(search_number, number_list[middle + 1])


setup = """
import random
"""
ss = """
def sequential_search(search_number, size):
    lists_of_numbers = [[random.randint(1,100) for number in range(100)] for number_list in range(size)]
    position = 0
    found = False
    for number_list in lists_of_numbers:
        while search_number < len(number_list) and not found:
            if number_list[position] == search_number:
                found = True
            else:
                position += 1
        return found
"""

oss = """
def ordered_sequential_search(search_number, size):
    lists_of_numbers = [[random.randint(1,100) for number in range(100)] for number_list in range(size)]
    position = 0
    found = False
    for number_list in lists_of_numbers:
        number_list = sorted(number_list)
        while position < len(number_list) and not found:
            if number_list[position] == search_number:
                found = True
            else:
                position += 1
        return found
"""

bsi = """
number_lists = [[random.randint(1,100) for number in range(100)] for number_list in range(100)]

def binary_search_iterative(search_number, lists_of_numbers=number_lists):
    found = False
    for number_list in lists_of_numbers:
        first_number, last_number = 0, len(number_list) - 1
        number_list = sorted(number_list)
        while first_number <= last_number and not found:
            middle = (first_number + last_number)//2
            if number_list[middle] == search_number:
                found = True
            elif search_number < number_list[middle]:
                last_number = middle - 1
            else:
                first_number = middle + 1
        return found
"""

bsr = """
def binary_search_recursive(search_number, size):
    lists_of_numbers = [[random.randint(1,100) for number in range(100)] for number_list in range(size)]
    for number_list in lists_of_numbers:
        number_list = sorted(number_list)
        if len(number_list) == 0:
            return False
        else:
            middle = len(number_lists)//2
        if number_list[middle] == search_number:
            return True
        elif search_number < number_list[middle]:
            return binary_search_recursive(search_number, number_list[:middle])
        else:
            return binary_search_recursive(search_number, number_list[middle + 1])
"""


def main():
    rt_avg_message = "{} Search took {} seconds to run, on average."
    searches = [
        ('Sequential', ss),
        ('Ordered Sequential', oss),
        ('Iterative Binary', bsi),
        ('Recursive', bsr)
        ]

    for search in searches:
        print(rt_avg_message.format(search[0], timeit.timeit(setup=setup, stmt=search[1], number=500)))
        print(rt_avg_message.format(search[0], timeit.timeit(setup=setup, stmt=search[1], number=10000)))
        print(rt_avg_message.format(search[0], timeit.timeit(setup=setup, stmt=search[1], number=10000)))


if __name__ == "__main__":
    main()
