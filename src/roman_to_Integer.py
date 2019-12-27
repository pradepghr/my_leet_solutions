# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is
# simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There are six instances where subtraction
# is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        skip = False
        for index, c in enumerate(s):
            if skip:
                skip = False
                continue

            if index < len(s) - 1:
                next = s[index + 1]
                if h[next] > h[c]:
                    num += h[next] - h[c]
                    skip = True
                    continue

            num += h[c]
        return num


# print(Solution().romanToInt('CMCD'))


# one dude's cool solution
#
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         # variable to store inter value
#         num = 0
#         # roman to decimal conversion
#
#         mapper = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
#         # adding value to decimal number for every character
#         for ch in s:   num += mapper[ch]
#
#         # subtraction rule
#
#         if 'CM' in s or 'CD' in s:   num -= 200
#
#         if 'XC' in s or 'XL' in s:   num -= 20
#
#         if 'IX' in s or 'IV' in s:   num -= 2
#
#         return num


print(Solution().romanToInt('CMCD'))
