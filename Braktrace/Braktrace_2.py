# 39. 组合总和 I
class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        res = []
        sorted(candidates)
        size = len(candidates)
        if target < 0 or size == 0:
            return res
        path = []
        self.backtrace(candidates, target, 0, size, res, path)
        return res

    def backtrace(self, candidates: [int], target: int, start: int, size: int, res: [int], path: [int]):
        if target < 0:
            return
        if target == 0:
            res.append(path[:])
            return

        for index in range(start, size):
            path.append(candidates[index])
            self.backtrace(candidates, target - candidates[index], index, size, res, path)
            path.pop()


# 40. 组合总和 II
class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        def backtrace(start: int, path: [], residue: int):
            if residue == 0:
                res.append(path[:])
                return
            for index in range(start, size):
                if candidates[index] > residue:
                    break

                if index > start and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                backtrace(index + 1, path, residue - candidates[index])
                path.pop()

        # sorted(candidates)
        candidates.sort()
        size = len(candidates)
        res = []
        path = []
        backtrace(0, path, target)
        return res


# 216. 组合总和 III
class Solution:
    def combinationSum3(self, k: int, n: int) -> [[int]]:
        def backtrace(k, residue, path, start):
            if residue == 0 and k == 0:
                res.append(path[:])
                return
            for index in range(start, 10):
                path.append(index)
                backtrace(k-1, residue-index, path, index+1)
                path.pop()

        res = []
        path = []
        backtrace(k, n, path, 1)
        return res
