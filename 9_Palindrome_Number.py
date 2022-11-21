
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s0 = str(x)
        len_ = len(s0)
        isPalindrom = True

        for i, digit in enumerate(s0):
            if digit != s0[len_-1-i]:
                isPalindrom = False

        return isPalindrom
s = Solution()
print(s.isPalindrome(13241))
