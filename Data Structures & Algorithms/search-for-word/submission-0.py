class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtrack + DFS
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, start):
            if start == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[start]:
                return False
            board[r][c] = '#'

            found = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if backtrack(nr, nc, start + 1):
                    found = True
                    break
            board[r][c] = word[start]
            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False