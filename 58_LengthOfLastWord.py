"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal

consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

 

Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_ptr = len(s) - 1
        last_letter = s[last_ptr]
        while last_ptr >= 0 and s[last_ptr] == " ":
            last_ptr -= 1
        first_ptr = last_ptr
        first_letter = s[first_ptr]
        while first_ptr >= 0 and s[first_ptr]!= " ":
            first_ptr -= 1

        last_word = s[first_ptr + 1:last_ptr + 1]
        return len(last_word)
    
my_solution = Solution()
my_solution.lengthOfLastWord("world")