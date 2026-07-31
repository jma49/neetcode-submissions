class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # DFS
        rows, cols = len(image), len(image[0])
        origin_color = image[sr][sc]
        
        if origin_color == color:
            return image

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols and image[r][c] == origin_color):
                return
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        dfs(sr, sc)
        return image
                    
                    