"""
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
--------------------------------
Example 1:

Input: colors = [0,1,0,1,0], k = 3

Output: 3
--------------------------------
Example 2:

Input: colors = [0,1,0,0,1,0,1], k = 6

Output: 2
--------------------------------
Example 3:

Input: colors = [1,1,0,1], k = 4

Output: 0
--------------------------------
Constraints:

3 <= colors.length <= 105
0 <= colors[i] <= 1
3 <= k <= colors.length
"""

from typing import List

## O(N * K) Solution
# class Solution:
#     def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
#         total_perfect_patterns = 0
#         #defensive unrolling
#         unrolled = colors[:] # creates a copy instead of a reference (unrolled = colors)
#         target_length = len(colors) + k - 1
#         while len(unrolled) < target_length:
#             unrolled += colors

#         for i in range(0, len(colors)):
#             # print(f'outer : {i}')
#             start = i + 1
#             # print(f'inner {start}')
#             # print("inner")
#             pattern_broken = False
#             for j in range(start, start + k - 1):
#                 # print(f"{j} is j, {j - 1} is j - 1")
#                 if unrolled[j - 1] == unrolled[j]:
#                     pattern_broken = True
#                     break
#             if pattern_broken == False:
#                 total_perfect_patterns += 1

#         return total_perfect_patterns


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:                  

        #this works only because of the constraint on k (3 <= k <= colors.length) otherwise we would need more defensive unrolling to prevent index errors
        unrolled = colors + colors
        for i in range(1, len(colors) + k):
            pass
            if unrolled[i - 1] != unrolled [i]:
                

s = Solution()
print(s.numberOfAlternatingGroups([0,1,0,1,0], 3))