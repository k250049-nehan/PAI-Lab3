def top_k_frequent(nums, k):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    result = sorted(freq, key=lambda x: freq[x], reverse=True)

    return result[:k]


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
