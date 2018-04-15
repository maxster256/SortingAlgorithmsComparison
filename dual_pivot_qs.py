# dual_quick_sort.py
import sys

class DualPivotQuickSort:
    'Dual Quick Sort implementation'

    def __init__(self):
        self._compares = 0
        self._shifts = 0

    def dual_quicksort(self, array, left, right):
        p = 0
        q = 0

        if right <= left:
            return
        if array[right] < array[left]:
            p = array[right]
            q = array[left]
            self._compares += 1
            sys.stderr.write("dual_quicksort: compare\n")
        else:
            p = array[left]
            q = array[right]
            self._compares += 1
            sys.stderr.write("dual_quicksort: compare\n")

        i = left + 1
        k = right - 1
        j = i
        d = 0

        while j <= k: #
            if d >= 0: #
                if array[j] < p: #
                    self._compares += 1
                    self._shifts += 1
                    sys.stderr.write("dual_quicksort: compare, shift\n")
                    array[i], array[j] = array[j], array[i]
                    i += 1
                    j += 1
                    d += 1
                else: #
                    if array[j] < q: #
                        self._compares += 1
                        sys.stderr.write("dual_quicksort: compare\n")
                        j += 1
                    else: #
                        self._compares += 1
                        self._shifts += 1
                        sys.stderr.write("quicksort: compare, shift\n")
                        array[j], array[k] = array[k], array[j]
                        k -= 1
                        d -= 1
            else: #
                if array[k] > q: #
                    self._compares += 1
                    sys.stderr.write("dual_quicksort: compare\n")
                    k -= 1
                    d -= 1
                else: #
                    if array[k] < p: #
                        temp = array[k]
                        array[k] = array[j]
                        array[j] = array[i]
                        array[i] = temp
                        i += 1
                        d += 1
                        self._compares += 1
                        self._shifts += 2
                        sys.stderr.write("dual_quicksort: compare, shift\n")
                    else:
                        array[j], array[k] = array[k], array[j]
                        self._compares += 1
                        self._shifts += 1
                        sys.stderr.write("dual_quicksort: compare, shift\n")

                    j += 1

        array[left] = array[i - 1]
        array[i - 1] = p
        array[right] = array[k + 1]
        array[k + 1] = q

        self.dual_quicksort(array, left, i - 2)
        self.dual_quicksort(array, i, k)
        self.dual_quicksort(array, k + 2, right)
