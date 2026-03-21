"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        triplets = []
        ptr_A = 0

        nums.sort()

        while ptr_A < len(nums) - 2:
            ptr_B = ptr_A + 1
            ptr_C = len(nums) - 1
            while ptr_B < ptr_C:
                sum = nums[ptr_A] + nums[ptr_B] + nums[ptr_C]
                if sum == 0:
                    triplet = [nums[ptr_A], nums[ptr_B], nums[ptr_C]]
                    triplets.append(triplet)
                    ptr_C -= 1
                    while ptr_B != ptr_C and nums[ptr_C] == nums[ptr_C + 1]:
                            ptr_C -= 1
                    ptr_B += 1
                    while ptr_B != ptr_B and nums[ptr_B] == nums[ptr_B - 1]:
                        ptr_B += 1
                elif sum > 0:
                    ptr_C -= 1
                else:
                    ptr_B += 1
            ptr_A += 1
            while ptr_A < len(nums) - 2 and nums[ptr_A] == nums[ptr_A - 1]:
                ptr_A += 1

        return triplets
                


#Example input
# nums = [-1,0,1,2,-1,-4]