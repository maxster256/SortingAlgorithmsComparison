import sys

class InsertionSort:
    'An implementation of the insertion sort'

    def __init__(self):
        self._compares = 0
        self._shifts = 0

    def insertionsort_asc(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1

            while j >= 0 and array[j] > key:
                self._compares += 1
                self._shifts += 1
                sys.stderr.write("insertionsort: compare, shift\n")

                array[j + 1] = array[j]
                j = j - 1
                array[j + 1] = key

            # Counts the additional comparison which will be performed upon exiting from the while loop.
            self._compares += 1
            sys.stderr.write("insertionsort: compare\n")

    def insertionsort_desc(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1

            while j >= 0 and array[j] < key:
                self._compares += 1

                array[j + 1] = array[j]
                j = j - 1
                array[j + 1] = key

                self._shifts += 1
                sys.stderr.write("insertionsort: compare, shift\n")

            # Counts the additional comparison which will be performed upon exiting from the while loop.
            self._compares += 1
            sys.stderr.write("insertionsort: compare\n")
