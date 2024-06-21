#Note this is a work in process - hard leetcode, trying to find a firrent way to do this than a sliding window

"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?

"""

# Smallest window in a String containing all characters of other strings
# Given two strings, string, and pattern, the task is to find the smallest substring in string containing all characters of pattern.

'''
Input: string = “this is a test string”, pattern = “tist”
Output: “t stri”
Explanation: “t stri” contains all the characters of pattern.

Input: string = “geeksforgeeks”, pattern = “ork”
Output: “ksfor”
'''

class Solution:
    def __init__(self, first_string, second_string):
        self.first_string = first_string
        self.second_string = second_string

    def smallest_window_substring(self):
        d = {}

        second_string_len = len(self.second_string)

        left_pointer = 0
        right_pointer = 0
        smallest_substring = ""
        # Create dictionary of values
        for i, f_char in enumerate(self.first_string):
            for s_char in self.second_string:
                if f_char == s_char:
                    if f_char not in d:
                        d[f_char] = [i]
                        if second_string_len == len(self.first_string):
                            left_pointer = i
                        second_string_len -= 1
                        if second_string_len == 0:
                            print("it contains the characters")
                            right_pointer = i
                            smallest_substring = self.first_string[slice(left_pointer, right_pointer + 1)]
                    # else:
                    #     for item in d:
                    #         if item != f_char:
                    #             for item


                        d[f_char].append(i)

        return smallest_substring

solution = Solution(first_string = "ADOBECODEBANC", second_string = "ABC")
result = solution.smallest_window_substring()
print(result)