
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [i, seen[remaining]]

            seen[value] = i

x = Solution()
nums = [1, 3, 4, 2]
target = 6
print('nums=' + str(nums), 'target='+str(target), 'answer='+ str(x.twoSum(nums, target)))

nums = [2, 7, 11, 15]
target = 9
print('nums=' + str(nums), 'target='+str(target), 'answer='+ str(x.twoSum(nums, target)))

nums = [3, 2, 4]
target = 6
print('nums=' + str(nums), 'target='+str(target), 'answer='+ str(x.twoSum(nums, target)))

nums = [3, 3]
target = 6
print('nums=' + str(nums), 'target='+str(target), 'answer='+ str(x.twoSum(nums, target)))

nums = [9, 2, 6, 4, 5, 3, 9]
target = 18
print('nums=' + str(nums), 'target='+str(target), 'answer='+ str(x.twoSum(nums, target)))
