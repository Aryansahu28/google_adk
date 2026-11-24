def quick_sort(arr):
    """
    Quick Sort Algorithm (Divide and Conquer)
    Time Complexity: O(n log n) average, O(n^2) worst
    Space Complexity: O(log n) auxiliary
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    sample_data = [10, 7, 8, 9, 1, 5]
    print("Original:", sample_data)
    print("Sorted:", quick_sort(sample_data))
