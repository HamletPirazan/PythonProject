def find_missing_number(nums):
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


print(find_missing_number([0, 1, 3]))
print(find_missing_number([4, 1, 3, 2, 0, 6, 7, 5]))
print(find_missing_number([9, 7, 2, 1, 0, 6, 8, 4, 5, 3]))
print(find_missing_number([]))
