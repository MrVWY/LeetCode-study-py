class Solution:
    # 198. 打家劫舍
    def rob(self, nums: [int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[-1]


class Solution:
    # 213. 打家劫舍 II
    def rob(self, nums: [int]) -> int:
        return max(self.robs(nums[:-1]), self.robs(nums[1:])) if len(nums) != 1 else nums[0]

    def robs(self, nums: [int]) -> int:
        dp_i = dp_i_1 = dp_i_2 = 0
        for num in nums:
            dp_i = max(dp_i_1, num + dp_i_2)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i


# Definition for a binary tree node.
# 337. 打家劫舍 III
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        select, unselect = self.robs(root)
        return max(select, unselect)

    def robs(self, cur: TreeNode) -> (int, int):
        if not cur:
            return 0, 0
        selectL, unselectL = self.robs(cur.left)
        selectR, unselectR = self.robs(cur.right)

        select = cur.val + unselectL + unselectR
        unselect = max(selectL, unselectL) + max(selectR, unselectR)
        return select, unselect
