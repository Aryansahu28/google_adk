def selection_sort(arr):
    """
    Selection Sort Algorithm
    Time Complexity: O(n^2) all cases
    Space Complexity: O(1) auxiliary
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    sample_data = [64, 25, 12, 22, 11]
    print("Original:", sample_data)
    print("Sorted:", selection_sort(sample_data))
