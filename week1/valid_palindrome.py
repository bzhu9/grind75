class Solution:
    def isPalindrome(self, s: str) -> bool:
        return "".join(letter for letter in s.lower() if letter.isalnum()) == "".join(letter for letter in s.lower() if letter.isalnum())[::-1]

