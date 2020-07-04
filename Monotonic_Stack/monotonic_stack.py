class Solution:
    def dailyTemperatures(self, T: [int]) -> [int]:
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperation = T[i]
            while stack and temperation > T[stack[-1]]:
                prevIndex = stack.pop()
                ans[prevIndex] = i - prevIndex
            stack.append(i)
        return ans



