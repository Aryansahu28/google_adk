def shell_sort(arr):
    """
    Shell Sort Algorithm (Generalized Insertion Sort)
    Time Complexity: O(n log n) best/average, O(n^2) worst depending on gap sequence
    Space Complexity: O(1) auxiliary
    """
    arr = arr.copy()
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


if __name__ == "__main__":
    sample_data = [12, 34, 54, 2, 3]
    print("Original:", sample_data)
    print("Sorted:", shell_sort(sample_data))
