import List


class Solution:
    # 136.只出现一次的数字
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a


class Solution:
    # 137. 只出现一次的数字 II
    def singleNumber(self, nums: List[int]) -> int:
        pass


class Solution:
    # 260. 只出现一次的数字 III
    def singleNumber(self, nums: List[int]) -> List[int]:
        bismask = 0
        for num in nums:
            bismask ^= num

        dift = bismask & (-bismask)
        x = 0
        for num in nums:
            # 分离出只出现一次的数字
            if num & dift:
                x ^= num
        return [x, bismask ^ x]
