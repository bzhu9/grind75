class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substring = ""
        for n in range(len(s)):
            if s[n] in substring:
                longest = max(longest, len(substring))
                substring = substring[substring.index(s[n]) + 1::]
            substring+=s[n]
        longest = max(longest, len(substring))
        return longest
