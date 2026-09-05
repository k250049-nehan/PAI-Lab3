def majority_element(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for num in freq:
        if freq[num] > len(nums) / 2:
            return num


print(majority_element([2, 2, 1, 2, 3, 2, 2]))
