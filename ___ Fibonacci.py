class Solution:
    def fibonachi(self, N: int) -> int:

        fb =[]
        for i in range(0, N):
            if i==0:
                fb.append(0)
            elif i==1:
                fb.append(1)
            else:
                fb.append(fb[i-1]+fb[i-2])

        return fb[len(fb)-1]

x = Solution()
print(x.fibonachi(6))
