class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():   # skip junk on left
                left += 1
            while left < right and not s[right].isalnum():  # skip junk on right
                right -= 1
            if s[left].lower() != s[right].lower():         # compare, case-insensitive
                return False
            left += 1
            right -= 1
        return True