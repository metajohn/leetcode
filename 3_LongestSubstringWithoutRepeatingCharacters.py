"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def determine_longest(self, ptrA, ptrB, longest):
        comparison_length = ptrB - ptrA + 1
        if longest < comparison_length:
            return comparison_length
        else:
            return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat_map = {}
        ptrA = 0
        ptrB = 0
        longest = 0


        for ptrB, ptrB_value in enumerate(s):
            if ptrB_value in repeat_map and repeat_map[ptrB_value] >= ptrA:
                ptrA = repeat_map[ptrB_value] + 1
            repeat_map[ptrB_value] = ptrB
            longest = self.determine_longest(ptrA, ptrB, longest)
        return longest


        
            

        