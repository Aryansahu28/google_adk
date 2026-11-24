def bucket_sort(arr):
    """
    Bucket Sort Algorithm (Useful for uniformly distributed floating point numbers in [0, 1))
    Time Complexity: O(n + k) average, O(n^2) worst
    Space Complexity: O(n + k)
    """
    if not arr:
        return []

    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]

    # Distribute input array elements into buckets
    min_val, max_val = min(arr), max(arr)
    val_range = (max_val - min_val) if max_val != min_val else 1

    for num in arr:
        # Normalize index to bucket range
        idx = int((num - min_val) / val_range * (num_buckets - 1))
        buckets[idx].append(num)

    # Sort individual buckets and concatenate
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr


if __name__ == "__main__":
    sample_data = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
    print("Original:", sample_data)
    print("Sorted:", bucket_sort(sample_data))
