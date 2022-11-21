class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i = 0
        max_i = 0
        for ch in s:
            if d.get(ch, None) is None:
                d[ch] = 1

        return max_i

x = Solution()

print(x.lengthOfLongestSubstring('dvdfdddvdfkdff'))
