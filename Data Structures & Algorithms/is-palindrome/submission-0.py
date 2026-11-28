class Solution:
    def isPalindrome(self, s: str) -> bool:
        final = ""
        for ch in s:
            if not ch.isalnum():
                continue
            final += ch.lower()

        return final == final[::-1]