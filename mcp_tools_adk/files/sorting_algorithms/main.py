from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from counting_sort import counting_sort
from radix_sort import radix_sort
from bucket_sort import bucket_sort
from shell_sort import shell_sort

if __name__ == "__main__":
    sample_ints = [64, 34, 25, 12, 22, 11, 90]
    sample_floats = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]

    print("=== Sorting Algorithms Demo ===\n")
    print("Original Int Array:", sample_ints)
    print("1. Bubble Sort:   ", bubble_sort(sample_ints))
    print("2. Selection Sort:", selection_sort(sample_ints))
    print("3. Insertion Sort:", insertion_sort(sample_ints))
    print("4. Merge Sort:    ", merge_sort(sample_ints))
    print("5. Quick Sort:    ", quick_sort(sample_ints))
    print("6. Heap Sort:     ", heap_sort(sample_ints))
    print("7. Counting Sort: ", counting_sort(sample_ints))
    print("8. Radix Sort:    ", radix_sort(sample_ints))
    print("9. Shell Sort:    ", shell_sort(sample_ints))
    print("\nOriginal Float Array:", sample_floats)
    print("10. Bucket Sort:  ", bucket_sort(sample_floats))
