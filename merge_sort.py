import sys

class MergeSort:
    'Merge sort implementation'

    def __init__(self):
        self._compares = 0
        self._shifts = 0

    # Performs the merging part of merge sort for the ascending algorithm
    def merge_asc(self, a, b):
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0] < b[0]:
                c.append(a[0])
                a.remove(a[0])

                sys.stderr.write("mergesort: shift, compare\n")
                self._compares += 1
                self._shifts += 1
            else:
                c.append(b[0])
                b.remove(b[0])

                sys.stderr.write("mergesort: shift, compare\n")
                self._compares += 1
                self._shifts += 1
        if len(a) == 0:
            c += b
            sys.stderr.write("mergesort: shift\n")
            self._shifts += 1
        else :
            c += a
            sys.stderr.write("mergesort: shift\n")
            self._shifts += 1
        return c

    # Performs the merging part of merge sort for the descending algorithm
    def merge_desc(self, a, b):
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0] > b[0]:
                c.append(a[0])
                a.remove(a[0])

                sys.stderr.write("mergesort: shift, compare\n")
                self._compares += 1
                self._shifts += 1
            else:
                c.append(b[0])
                b.remove(b[0])

                sys.stderr.write("mergesort: shift, compare\n")
                self._compares += 1
                self._shifts += 1
        if len(a) == 0:
            c += b
            sys.stderr.write("mergesort: shift\n")
            self._shifts += 1
        else :
            c += a
            sys.stderr.write("mergesort: shift")
            self._shifts += 1
        return c

    # Mergesort, which sorts the list in the ascending order
    def mergesort_asc(self, array):
        if len(array) < 2:
            return array
        else:
            middle = int(len(array)/2)
            a = self.mergesort_asc(array[:middle])
            b = self.mergesort_asc(array[middle:])

            return self.merge_asc(a, b)

    # Mergesort, which sorts the list in the descending order
    def mergesort_desc(self, array):
        if len(array) < 2:
            return array
        else:
            middle = int(len(array)/2)
            a = self.mergesort_desc(array[:middle])
            b = self.mergesort_desc(array[middle:])

            return self.merge_desc(a, b)
