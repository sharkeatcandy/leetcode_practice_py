# https://leetcode.com/problems/length-of-last-word/description/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_split_with_space = s.split(" ")
        s_split_with_space = list(filter(None, s_split_with_space))
        return len(s_split_with_space[-1])
