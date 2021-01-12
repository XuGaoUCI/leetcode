class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        left, right, upper, lower = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        direction = 0
        while True:
            if direction == 0:
                for j in range(left, right + 1):
                    res.append(matrix[upper][j])
                upper += 1
            if direction == 1:
                for j in range(upper, lower + 1):
                    res.append(matrix[j][right])
                right -= 1
            if direction == 2:
                for j in range(right, left - 1, -1):
                    res.append(matrix[lower][j])
                lower -= 1
            if direction == 3:
                for j in range(lower, upper - 1, -1):
                    res.append(matrix[j][left])
                left += 1
            if left > right or upper > lower:
                break
            direction = (direction + 1) % 4
        return res

            
        
        
