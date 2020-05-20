class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        num_freq = collections.Counter(nums)
        sum_tb = collections.Counter()
        for num in nums:
            if num_freq[num] == 0:
                continue
            num_freq[num] -= 1
            cnt = 1
            while cnt < k and num + cnt in num_freq:
                cnt += 1
            if cnt == k:
                for i in range(1, k):
                    num_freq[num+i] -= 1
                sum_tb[num+k-1] += 1
            else:
                return False
        return True
