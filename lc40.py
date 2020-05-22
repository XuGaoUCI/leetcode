# notes
# comapred to combination sum I: change j to j+1 and use j!= idx and nums[j-1] == nums[j] to remove duplicates.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.recursion(target, 0, [], candidates, res)
        return res
    def recursion(self, remainsum, idx, currentlst, nums, res):
        if remainsum < 0:
            return
        if remainsum == 0:
            res.append(currentlst)
            return
        for j in range(idx, len(nums)):
            if j!= idx and nums[j-1] == nums[j]:
                continue
            self.recursion(remainsum - nums[j], j+1, currentlst+[nums[j]], nums, res)
            
            
        
