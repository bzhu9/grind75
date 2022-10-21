class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        unique = set(s)
        for letter in unique:
            count += 2 * (s.count(letter)//2)
        return count if count == len(s) else count + 1
