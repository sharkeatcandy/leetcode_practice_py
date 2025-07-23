# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        sum_number = 0
        i = 0
        while i < len(s):
            print(sum_number)
            print(i)
            print(s[i])
            if s[i] == "M":
                sum_number += 1000
            elif s[i] == "D":
                sum_number += 500
            elif s[i] == "L":
                sum_number += 50
            elif s[i] == "V":
                sum_number += 5
            elif s[i] == "C":
                if i + 1 < len(s):
                    if s[i + 1] == "D":
                        sum_number += 400
                        i += 2
                        continue
                    elif s[i + 1] == "M":
                        sum_number += 900
                        i += 2
                        continue
                sum_number += 100
            elif s[i] == "X":
                if i + 1 < len(s):
                    if s[i + 1] == "L":
                        sum_number += 40
                        i += 2
                        continue
                    elif s[i + 1] == "C":
                        sum_number += 90
                        i += 2
                        continue
                sum_number += 10
            elif s[i] == "I":
                if i + 1 < len(s):
                    if s[i + 1] == "V":
                        sum_number += 4
                        i += 2
                        continue
                    elif s[i + 1] == "X":
                        sum_number += 9
                        i += 2
                        continue
                sum_number += 1
            i += 1
        return sum_number
