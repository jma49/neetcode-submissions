class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        ans = []

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            
            for j in range(top, bottom + 1):
                ans.append(matrix[j][right])
            right -= 1
            
            if top <= bottom:
                for k in range(right, left - 1, -1):
                    ans.append(matrix[bottom][k])
                bottom -= 1

            if left <= right:
                for l in range(bottom, top - 1, -1):
                    ans.append(matrix[l][left])
                left += 1
            
        return ans


