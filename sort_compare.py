"""
====================================
Part 2 - Search Algorithm Comparison
====================================
1. Create a 'sort_compare.py' file.
2. Create 3 functions using the codes from the 'Sorting' section:
    a. insertion_sort
    b. shell_sort
    c. python_sort ('wrapper' function that calls sort on input list)
3. Modify each code to calculate the time required to sort.
4. The program's main function is to call these return how long the function
takes on average to sort the lists (sizes 500, 1000, and 10000).
    a. The results should display: 'Sequential Search Took % 10.7f seconds to
    run on average.'
-----------------------
Functional Requirements
-----------------------
a. Define the thee functions insertion_search_shell, shell_sort, and
 python_sort).
b. The functions should return the appropriate values.
c. Define a main() function that will print out the results.
"""

import random
import timeit

results_message = "{} sort took {} seconds, run on average."


def insertion_sort(size):
    number_lists = [[random.randint(1, 100) for number in range(100)] for number_list in range(size)]
    sorted_lists = []
    for number_list in number_lists:
        for index in range(1, len(number_list)):
            current_value = number_list[index]
            position = index
            while position > 0 and number_list[position - 1] > current_value:
                number_list[position] = number_list[position - 1]
                position -= 1
                number_list[position] = current_value
        sorted_lists.append(number_list)
    return sorted_lists


def shell_sort(size):
    number_lists = [[random.randint(1, 100) for number in range(100)] for number_list in range(size)]
    sorted_lists = []
    count = 0
    for number_list in number_lists:
        for index in range(1, len(number_list)):
            sublist_count = len(number_list) // 2
            while sublist_count > 0:
                for start_position in range(sublist_count):
                    # beginning
                    for i in range(start_position + sublist_count, len(number_list), sublist_count):
                        current_value = number_list[i]
                        position = i
                    while position >= sublist_count and number_list[position - sublist_count] > current_value:
                        number_list[position] = number_list[position - sublist_count]
                        position -= sublist_count
                        number_list[position] = current_value
                        # end
                sublist_count //= 2
        sorted_lists.append(number_list)
        print(number_list)
    return sorted_lists


def python_sort(size):
    number_lists = [[random.randint(1, 100) for number in range(100)] for number_list in range(size)]
    sorted_lists = []
    for number_list in number_lists:
        sorted_lists.append(sorted(number_list))
    return sorted_lists


setup = """
import random
import timeit
"""

insertion = """
def insertion_sort(size):
    number_lists = [[random.randint(1, 100) for number in range(100)] for number_list in range(size)]
    sorted_lists = []
    for number_list in number_lists:
        for index in range(1, len(number_list)):
            current_value = number_list[index]
            position = index
            while position > 0 and number_list[position - 1] > current_value:
                number_list[position] = number_list[position - 1]
                position -= 1
                number_list[position] = current_value
        sorted_lists.append(number_list)
    return sorted_lists
"""

shell = """
def shell_sort(size):
    number_lists = [[random.randint(1, 100) for number in range(100)] for number_list in range(size)]
    sorted_lists = []
    count = 0
    for number_list in number_lists:
        for index in range(1, len(number_list)):
            sublist_count = len(number_list) // 2
            while sublist_count > 0:
                for start_position in range(sublist_count):
                    # beginning
                    for i in range(start_position + sublist_count, len(number_list), sublist_count):
                        current_value = number_list[i]
                        position = i
                    while position >= sublist_count and number_list[position - sublist_count] > current_value:
                        number_list[position] = number_list[position - sublist_count]
                        position -= sublist_count
                        number_list[position] = current_value
                        # end
                sublist_count //= 2
        sorted_lists.append(number_list)
        print(number_list)
    return sorted_lists
"""

python =  """
def python_sort(size):
    number_lists = [[random.randint(1, 100) for number in range(100)] for number_list in range(size)]
    sorted_lists = []
    for number_list in number_lists:
        sorted_lists.append(sorted(number_list))
    return sorted_lists
"""


def main():
    rt_avg_message = "{} Sort took {} seconds to run, on average."
    searches = [
        ('Insertion', insertion),
        ('Shell', shell),
        ('Python', python)
        ]

    for search in searches:
        print(rt_avg_message.format(search[0], timeit.timeit(setup=setup, stmt=search[1], number=500)))
        print(rt_avg_message.format(search[0], timeit.timeit(setup=setup, stmt=search[1], number=10000)))
        print(rt_avg_message.format(search[0], timeit.timeit(setup=setup, stmt=search[1], number=10000)))


if __name__ == "__main__":
    # for numb_list in insertion_search_shell():
    #    print(numb_list)
    # iss = Timer("insertion_search_shell()", "from __main__ import insertion_search_shell")
    # ss = Timer("shell_sort()", "from __main__ import shell_sort")
    # ips = Timer("python_sort()", "from __main__ import python_sort")

    # print("insertion_sort: ", iss.timeit(number=1000), "milliseconds")
    # print(results_message.format("Shell ", ss.timeit(number=1000)))
    # print("python_sort: ", ps.timeit(number=1000), "milliseconds")
    #for row in shell_sort():
    #    print(row)
    shell_sort()