"""
prefix sum is effectively a way of deriving the distance between subsets
because all of the values are pre-processed in to the prefix array
distance can be accessed in O(1)
"""

nums = [1]
nums = nums * 10
print(f'original array:  {nums}')

# assign the first value of the prefix to the first value of the array
prefix = [nums[0]]
# iterate through the array starting at 1
for i in range(1, len(nums)):
    # append the ith value from the array plus the last value from prefix
    prefix.append(nums[i] + prefix[len(prefix) - 1])

print(f'prefix array:    {prefix}')

distance = prefix[1] - prefix[0]
print(f'distance:        {distance}')