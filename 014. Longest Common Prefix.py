
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
print(arr, 'ans=', x.longestCommonPrefix(arr))

arr = ["dog","racecar","car"]
print(arr, 'ans=', x.longestCommonPrefix(arr))

arr = []
print(arr, 'ans=', x.longestCommonPrefix(arr))

arr = ['q', 'q', '']
print(arr, 'ans=', x.longestCommonPrefix(arr))
