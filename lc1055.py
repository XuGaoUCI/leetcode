class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_set = set(source)
        # two pointers
        res = 0
        left, right = 0, 0
        while right < len(target):
            if target[right] not in source_set:
                return -1
            if left == len(source):
                res += 1
                left = 0
            elif source[left] == target[right]:
                left += 1
                right += 1
            else:
                while left < len(source) and source[left] != target[right]:
                    left += 1
                if left == len(source):
                    left = 0
                    res += 1
                else:
                    left += 1
                    right += 1
        return res + 1 
        
