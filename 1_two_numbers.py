class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # O(n2) Solution
        # weFindIt = False
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             weFindIt = True
        #             break
        #     if weFindIt:
        #         break
        #
        # if weFindIt:
        #     return [i, j]

        # fast Solution
        dict_ = {}
        i=0
        len_ = len(nums)

        # build dict {number:position} in reverse order with respect to list
        while i<len_:
            if dict_.get(nums[len_-1-i], -1) < 0:
                dict_[nums[len_-1-i]] = len_-1-i
            i+=1

        # find first pare in dict for each number in list and check for exclude dublicates
        i=0
        while i<len_:
            if dict_.get(target - nums[i], -1) > 0 and i != dict_.get(target - nums[i], -1):
                return [i, dict_.get(target-nums[i])]
            i+=1

        return [-1, -1]

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
