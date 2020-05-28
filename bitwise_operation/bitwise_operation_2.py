# 78. 子集
import List


class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        res, total = [], 1 << len(nums)
        for i in range(total):
            a = []
            num, index = i, 0
            while num:
                if num & 1:
                    a.append(nums[index])
                num = num >> 1
                index += 1
            res.append(a)
        return res


# 90. 子集 II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, total = [], 1 << len(nums)
        sorted(nums)
        for i in range(total):
            a = []
            flag = True
            for j in range(len(nums)):
                if (i >> j) & 1:
                    if j > 0 and nums[j] == nums[j-1] and (i >> (j - 1)) & 1 :
                        flag = False
                        break
                    else:
                        a.append(nums[j])
            if flag:
                res.append(a)
        return res
