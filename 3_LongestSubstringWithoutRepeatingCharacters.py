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
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptrA = 0
        ptrB = ptrA

        if len(s) != 0:
            longest_length = 1
        else:
            return 0

        #if within the range of s - the longest substring known, because if it is less than nothing can be larger...
        while ptrA < len(s) - longest_length:
            # while within the string moving B right check for duplicates to avoid modifying the map
            while ptrB + 1 < len(s) and s[ptrA + 1] == s[ptrA]:
                ptrA += 1
                ptrB = ptrA

            #reset the map for comaparing previous values
            found_map = {}
            found_map[s[ptrA]] = ptrA

            #while within the string, and the next character is not a known value, move B right
            while ptrB + 1 < len(s) and s[ptrB + 1] not in found_map:
                ptrB += 1
                found_map[s[ptrB]] = ptrB
                #adding B to the map for each new value

            #if the difference is greater we have a new longest substring
            if (len(found_map)) > longest_length:
                longest_length = len(found_map)

            #get the index of the earliest current matching duplicate and try to start at the next value in the string
            if ptrB + 1 < len(s):
                ptrA = found_map[s[ptrB + 1]] + 1
            else:
                break
        return longest_length


s = Solution()
print(s.lengthOfLongestSubstring("anvianj"))


        
            

        