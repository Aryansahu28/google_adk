def insertion_sort(arr):
    """
    Insertion Sort Algorithm
    Time Complexity: O(n^2) worst/average, O(n) best
    Space Complexity: O(1) auxiliary
    """
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    sample_data = [12, 11, 13, 5, 6]
    print("Original:", sample_data)
    print("Sorted:", insertion_sort(sample_data))
