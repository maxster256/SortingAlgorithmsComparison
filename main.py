# sorting.py

def check_sort_order_asc(array):
    if sorted(array) == array:
        print("List is sorted correctly.")
    else:
        print("List is not sorted correctly.")

def check_sort_order_desc(array):
    if sorted(array, reverse=True) == array:
        print("List is sorted correctly.")
    else:
        print("List is not sorted correctly.")


# Imports
from insertion_sort import InsertionSort
from quick_sort import QuickSort
from merge_sort import MergeSort
from dual_pivot_qs import DualPivotQuickSort

import random
import argparse
import sys
import time

import numpy as np
import pandas as pd

from timeit import default_timer as timer

# sys.setrecursionlimit(2000)

parser = argparse.ArgumentParser()

parser.add_argument(
    '--type',
    choices=('quick', 'merge', 'insert', 'dual'),
    default='quick',
)

parser.add_argument(
    '--comp',
    choices=('<=', '>='),
    default='<=',
)

parser.add_argument(
    '--stat',
    nargs = 2,
    type = str,
)

args = parser.parse_args()

if args.stat != None:
    # Perform statistical operations

    output_file = args.stat[0]
    repetitions = int(args.stat[1])

    qsort = np.zeros(shape=(100*repetitions, 5))
    merge = np.zeros(shape=(100*repetitions, 5))
    insert = np.zeros(shape=(100*repetitions, 5))

    array_index = 0

    for k in range(0, repetitions):

        for n in range(100, 10100, 100):
            random_data = random.sample(range(n), n)

            qsort_data  = random_data
            merge_data  = random_data
            insert_data = random_data
            dqsort_data = random_data

            # Perform QuickSort on our randomly-generated data
            q_sorting = QuickSort()

            start = time.time()
            q_sorting.quick_sort(qsort_data, 0, len(qsort_data) - 1)
            end = time.time()
            elapsed = end - start

            qsort[array_index] = [k, n, q_sorting._compares, q_sorting._shifts, elapsed]

            # Perform MergeSort on our randomly-generated data
            m_sorting = MergeSort()

            start = time.time()
            result = m_sorting.mergesort_asc(merge_data)
            end = time.time()
            elapsed = end - start

            merge[array_index] = [k, n, m_sorting._compares, m_sorting._shifts, elapsed]

            # Perform InsertionSort on our randomly-generated data
            i_sorting = InsertionSort()

            start = time.time()
            i_sorting.insertionsort_asc(insert_data)
            end = time.time()
            elapsed = end - start

            insert[array_index] = [k, n, i_sorting._compares, i_sorting._shifts, elapsed]

            # Don't forget to increment the index
            array_index += 1

    # Uses Pandas' DataFrame to save the results in CSV files
    # This way the conversion will be much, much quicker, but will use up more memory.
    qp = pd.DataFrame(qsort, columns = ["Trial", "Size", "Comparisons", "Swaps", "QuickSort duration"])
    qp.to_csv(output_file + "_quicksort.csv")

    mp = pd.DataFrame(merge, columns = ["Trial", "Size", "Comparisons", "Swaps", "Merge duration"])
    mp.to_csv(output_file + "_merge.csv")

    ip = pd.DataFrame(insert, columns = ["Trial", "Size", "Comparisons", "Swaps", "Insert duration"])
    ip.to_csv(output_file + "_insert.csv")

    # Save all the results in one file
    with open(output_file + ".csv", 'w') as f:
        pd.concat([qp, mp, ip], axis=1).to_csv(f)

else:
    # Perform sorting on data given by the user

    numbers_count = int(input().split()[0])
    numbers = [int(part) for part in input().split()]

    if len(numbers) != numbers_count:
        print("error: invalid number of arguments provided.")
        exit(0)

    sorting = None

    if args.comp == '<=':
        # Default sorting order (ascending)
        # -4 156 -97 13 2
        if args.type == 'merge':
            sorting = MergeSort()

            start = time.time()
            result = sorting.mergesort_asc(numbers)
            end = time.time()
            elapsed = end - start

            sys.stderr.write("Sorting finished.\nTotal shifts = " + str(sorting._shifts) + ", comparisions = " + str(sorting._compares) + ", time elapsed = " + str(elapsed) + " seconds.\n")

            check_sort_order_asc(result)
            print("Sorted " + str(len(numbers)) + " elements, result: " + str(result))

        elif args.type == 'insert':
            sorting = InsertionSort()

            start = time.time()
            sorting.insertionsort_asc(numbers)
            end = time.time()
            elapsed = end - start

            sys.stderr.write("Sorting finished.\nTotal shifts = " + str(sorting._shifts) + ", comparisions = " + str(sorting._compares) + ", time elapsed = " + str(elapsed) + " seconds.\n")

            check_sort_order_asc(numbers)
            print("Sorted " + str(len(numbers)) + " elements, result: " + str(numbers))

        elif args.type == 'dual':
            sorting = DualPivotQuickSort()

            start = time.time()
            sorting.dual_quicksort(numbers, 0, numbers_count-1)
            end = time.time()
            elapsed = end - start

            sys.stderr.write("Sorting finished.\nTotal shifts = " + str(sorting._shifts) + ", comparisions = " + str(sorting._compares) + ", time elapsed = " + str(elapsed) + " seconds.\n")

            check_sort_order_asc(numbers)
            print("Sorted " + str(len(numbers)) + " elements, result: " + str(numbers))

        else:
            sorting = QuickSort()

            start = time.time()
            sorting.quick_sort(numbers, 0, numbers_count-1)
            end = time.time()
            elapsed = end - start

            sys.stderr.write("Sorting finished.\nTotal shifts = " + str(sorting._shifts) + ", comparisions = " + str(sorting._compares) + ", time elapsed = " + str(elapsed) + " seconds.\n")

            check_sort_order_asc(numbers)
            print("Sorted " + str(len(numbers)) + " elements, result: " + str(numbers))
    elif args.comp == '>=':
        # Descending sorting order
        if args.type == 'merge':
            sorting = MergeSort()

            start = time.time()
            result = sorting.mergesort_desc(numbers)
            end = time.time()
            elapsed = end - start

            sys.stderr.write("Sorting finished.\nTotal shifts = " + str(sorting._shifts) + ", comparisions = " + str(sorting._compares) + ", time elapsed = " + str(elapsed) + " seconds.\n")

            check_sort_order_desc(result)
            print("Sorted " + str(len(numbers)) + " elements, result: " + str(result))

        elif args.type == 'insert':
            sorting = InsertionSort()

            start = time.time()
            sorting.insertionsort_desc(numbers)
            end = time.time()
            elapsed = end - start

            sys.stderr.write("Sorting finished.\nTotal shifts = " + str(sorting._shifts) + ", comparisions = " + str(sorting._compares) + ", time elapsed = " + str(elapsed) + " seconds.\n")

            check_sort_order_desc(numbers)
            print("Sorted " + str(len(numbers)) + " elements, result: " + str(numbers))

        elif args.type == 'dual':
            sorting = DualPivotQuickSort()

            start = time.time()
            sorting.dual_quicksort(numbers, 0, numbers_count-1)
            end = time.time()
            elapsed = end - start

            sys.stderr.write("Sorting finished.\nTotal shifts = " + str(sorting._shifts) + ", comparisions = " + str(sorting._compares) + ", time elapsed = " + str(elapsed) + " seconds.\n")

            check_sort_order_asc(sorted(numbers, reverse=True))
            print("Sorted " + str(len(numbers)) + " elements, result: " + str(sorted(numbers, reverse=True)))

        else:
            sorting = QuickSort()

            start = time.time()
            sorting.quick_sort_desc(numbers, 0, numbers_count-1)
            end = time.time()
            elapsed = end - start

            sys.stderr.write("Sorting finished.\nTotal shifts = " + str(sorting._shifts) + ", comparisions = " + str(sorting._compares) + ", time elapsed = " + str(elapsed) + " seconds.\n")

            check_sort_order_desc(numbers)
            print("Sorted " + str(len(numbers)) + " elements, result: " + str(numbers))
