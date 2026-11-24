def _counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output


def radix_sort(arr):
    """
    Radix Sort Algorithm (Non-comparison sort for non-negative integers)
    Time Complexity: O(d * (n + b)) where d is max digits, b is base (10)
    Space Complexity: O(n + b)
    """
    if not arr:
        return []

    arr = arr.copy()
    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        arr = _counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr


if __name__ == "__main__":
    sample_data = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original:", sample_data)
    print("Sorted:", radix_sort(sample_data))
