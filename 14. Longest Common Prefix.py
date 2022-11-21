
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        cprefix = ''
        k = True
        i = 0

        while k :
            try:
                s = strs[0][i]
            except IndexError:
                k = False
                break

            for str_ in strs:
                try:
                    if str_[i] != s:
                        k = False
                        break
                except IndexError:
                    k = False
                    break

            if k:
                cprefix += s
            i+=1

        return cprefix

x = Solution()
arr = ["flower","flow","flight"]
arr = ["dog","racecar","car"]
arr = []
arr = ['q', 'q', '']
print(x.longestCommonPrefix(arr))