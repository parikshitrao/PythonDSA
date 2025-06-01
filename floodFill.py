class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, colums = len(image), len(image[0])
        original = image[sr][sc]
        if original == color:
            return image
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=colums:
                return
            if original != image[r][c]:
                return
            image[r][c] = color
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r,c+1)
        dfs(sr,sc)
        return image