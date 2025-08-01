# HOMEWORK06 for CS132SP_2025

import random

# Quick sort borrowed from textbook
def quick_sort(a_list):
    c, a = quick_sort_helper(a_list, 0, len(a_list) - 1, 0, 0)
    return f"({emptySpace(c)},{emptySpace(a)})"

def quick_sort_helper(a_list, first, last, c, a):
    if first < last:
        split, c, a = partition(a_list, first, last, c, a)
        c, a = quick_sort_helper(a_list, first, split - 1, c, a)
        c, a = quick_sort_helper(a_list, split + 1, last, c, a)
    return c, a

def partition(a_list, first, last, c, a):
    pivot_val = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            c += 1
            left_mark = left_mark + 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            c += 1
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = (
                a_list[right_mark],
                a_list[left_mark],
            )
            a += 2
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]
    a += 2

    return right_mark, c, a

# Merge Sort borrowed from textbook
def merge_sort(a_list, a=0, c=0):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        a += 2

        c, a = merge_sort(left_half, a, c)
        c, a = merge_sort(right_half, a, c)

        i, j, k = 0, 0, 0
        # a = a + 3
        while i < len(left_half) and j < len(right_half):
            c += 1
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
                a += 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
                a += 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1
            a += 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
            a += 1

    return c, a

# Shell sort borrowed from textbook
def shell_sort(a_list):
    a = 0
    c = 0
    sublist_count = len(a_list) // 2
    a += 1
    while sublist_count > 0:
        c += 1
        for pos_start in range(sublist_count):
            a, c = gap_insertion_sort(a_list, pos_start, sublist_count, a, c)
        sublist_count = sublist_count // 2
        a += 1
    
    return f"({emptySpace(c)},{emptySpace(a)})"

def gap_insertion_sort(a_list, start, gap, a, c):
    for i in range(start + gap, len(a_list), gap):
        cur_val = a_list[i]
        cur_pos = i
        a += 2
        while cur_pos >= gap and a_list[cur_pos - gap] > cur_val:
            c += 2
            a_list[cur_pos] = a_list[cur_pos - gap]
            cur_pos = cur_pos - gap
            a += 2
        a_list[cur_pos] = cur_val
        a += 1
        return a, c

# Insertion Sort borrowed from textbook
def insertion_sort(a_list):
    c = 0
    a = 0
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i
        a += 1
        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos = cur_pos - 1
            a, c = (a + 1), (c + 1)
        a_list[cur_pos] = cur_val
        a += 1

    return f"({emptySpace(c)},{emptySpace(a // 2)})"

# Selection sort borrowed from the textbook
def selection_sort(a_list):
    # Equation to calculate comparisons (n(n -1)/2) same as bubble sort
    c = len(a_list) * (len(a_list) - 1) // 2
    a = 0
    for i, item in enumerate(a_list):
        min_idx = len(a_list) - 1
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_idx]:
                min_idx = j
        if min_idx != i:
            a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]
            a += 2
    
    return f"({emptySpace(c)},{emptySpace(a)})"
    
# Bubble sort borrowed from textbook
def bubble_sort_short(a_list):
    # Equation to calculate comparisons (n(n -1)/2)
    # https://testbook.com/question-answer/what-is-the-formula-to-be-used-to-calculate-the-to--61a9fa0c25363842160e93a0#:~:text=To%20understand%20the%20bubble%20sort,of%20comparisons%20will%20n%2D1.&text=Total%20number%20comparisons%20till%20kth%20iterations%20%3D%20k(n)%2D(,%2B4%2B....
    c = len(a_list) * (len(a_list) - 1) // 2
    # Assignement counter initialization
    a = 0
    for i in range(len(a_list) - 1, 0, -1):
        exchanges = False
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                exchanges = True
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                a += 2
        if not exchanges:
            break
        
    return f"({emptySpace(c)},{emptySpace(a)})"

# A function to make the ouput print match the example in the modules
def emptySpace(val):
    empty_space_1 = (8 - len(str(val))) * " "
    return empty_space_1 + str(val)

# Random list generation
def randomList(val):
    ranList = []
    for i in range(val):
        ranVal = random.randint(1, val)
        ranList.append(ranVal)
    
    return ranList

# Main funciton
def main():
    print("""Number of list comparisons and assignments for Chapter 6 sorting algorithms on identical random lists of N elements
(NOTE: use of temp variables in swaps replaced by simultaneous assignment)
          
    N     Bubble Sort        Selection Sort      Insertion Sort        Shell Sort          Merge Sort          Quick Sort    
      (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns) """)
    c, a = merge_sort(randomList(10))
    c, a = emptySpace(c), emptySpace(a)   
    print(f"""   10 {bubble_sort_short(randomList(10))} {selection_sort(randomList(10))} {insertion_sort(randomList(10))} {shell_sort(randomList(10))} ({c},{a}) {quick_sort(randomList(10))}""")
    c, a = merge_sort(randomList(100))
    c, a = emptySpace(c), emptySpace(a)
    print(f"""  100 {bubble_sort_short(randomList(100))} {selection_sort(randomList(100))} {insertion_sort(randomList(100))} {shell_sort(randomList(100))} ({c},{a}) {quick_sort(randomList(100))}""")
    c, a = merge_sort(randomList(1000))
    c, a = emptySpace(c), emptySpace(a)
    print(f""" 1000 {bubble_sort_short(randomList(1000))} {selection_sort(randomList(1000))} {insertion_sort(randomList(1000))} {shell_sort(randomList(1000))} ({c},{a}) {quick_sort(randomList(1000))}""")
    c, a = merge_sort(randomList(10000))
    c, a = emptySpace(c), emptySpace(a)
    print(f"""10000 {bubble_sort_short(randomList(10000))} {selection_sort(randomList(10000))} {insertion_sort(randomList(10000))} {shell_sort(randomList(10000))} ({c},{a}) {quick_sort(randomList(10000))}""")
    
main()

# Had to look up what simultaneous assignment was 
# https://stackoverflow.com/questions/16409901/simultaneous-assignment-semantics-in-python
