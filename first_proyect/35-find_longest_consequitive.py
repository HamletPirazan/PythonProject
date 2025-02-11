def longest_consecutive_subsequence(nums):
    if not nums:
        return []
    ordered_list = sorted(set(nums))
    longest = 1
    current_length = 1

    for i in range(1, len(ordered_list)):
        if ordered_list[i] == ordered_list[i-1]  + 1:
            current_length +=1
        else:
            longest = max(longest, current_length)
            current_length = 1
    return max(longest, current_length)

print(longest_consecutive_subsequence([100, 4, 200, 1, 3, 2]))
print(longest_consecutive_subsequence([5, 2, 99, 3, 4, 1]))
print(longest_consecutive_subsequence([1, 2, 3, 4, 5]))
print(longest_consecutive_subsequence([5, 4, 3, 2, 1]))
print(longest_consecutive_subsequence([]))