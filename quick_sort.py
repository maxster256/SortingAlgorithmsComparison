import sys

class QuickSort:
    'Quick sort implementation'

    def __init__(self):
        self._compares = 0
        self._shifts = 0

    def partition(self, array, start, end):
        pivot = array[end] # can be randomized
        partition_index = start

        for i in range(start, end):
            if array[i] <= pivot:
                # Swaps list[i] and list[partition_index]
                array[i], array[partition_index] = array[partition_index], array[i]
                partition_index += 1
                self._compares += 1
                self._shifts += 1
                sys.stderr.write("quicksort: compare, shift\n")

        # Swaps list[partition_index] and list[end]
        array[partition_index], array[end] = array[end], array[partition_index]
        self._shifts += 1
        sys.stderr.write("quicksort: shift\n")

        return partition_index

    def quick_sort(self, array, start, end):
        if (start < end):
            partition_index = self.partition(array, start, end)
            self.quick_sort(array, start, partition_index-1)
            self.quick_sort(array, partition_index+1, end)

    def partition_desc(self, array, start, end):
        pivot = array[end] # can be randomized
        partition_index = start

        for i in range(start, end):
            if array[i] >= pivot:
                # Swaps list[i] and list[partition_index]
                array[i], array[partition_index] = array[partition_index], array[i]
                partition_index += 1

                self._compares += 1
                self._shifts += 1
                sys.stderr.write("quicksort: compare, shift\n")

        # Swaps list[partition_index] and list[end]
        array[partition_index], array[end] = array[end], array[partition_index]
        self._shifts += 1
        sys.stderr.write("quicksort: shift\n")

        return partition_index

    def quick_sort_desc(self, array, start, end):
        if (start < end):
            partition_index = self.partition_desc(array, start, end)
            self.quick_sort_desc(array, start, partition_index-1)
            self.quick_sort_desc(array, partition_index+1, end)

    # Python-esque QuickSort for reference
    # def quicksort(arr):
    #     if len(arr) <= 1:
    #         return arr
    #     pivot = arr[len(arr) // 2]
    #     left = [x for x in arr if x < pivot]
    #     middle = [x for x in arr if x == pivot]
    #     right = [x for x in arr if x > pivot]
    #     return quicksort(left) + middle + quicksort(right)
