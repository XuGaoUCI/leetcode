# Notes:
#   1.can not use currentlst.append()  recursion  currentlst.pop() b/c Python will change them by reference, it will change them all
#   2. can not do return res.append(currentlst) as this is not to return res
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #dfs
        res = []
        self.recursion(target, 0, [], res, candidates)
        return res
        
    def recursion(self, remainsum, idx, currentlst, res, nums):
        if remainsum < 0:
            return
        if remainsum == 0:
            res.append(currentlst)
            return
        for j in range(idx, len(nums)):
            self.recursion(remainsum - nums[j], j, currentlst + [nums[j]], res, nums)
