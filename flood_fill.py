class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        firstColor = image[sr][sc]
        visited = set()
        def flood(r,c):
            if r < 0 or r > len(image) - 1 or c < 0 or c > len(image[0]) - 1 or image[r][c] != firstColor or (r,c) in visited:
                return
            image[r][c] = color
            visited.add((r,c))
            flood (r + 1, c)
            flood (r - 1, c)
            flood (r, c + 1)
            flood (r, c - 1)
        flood(sr,sc)
        return image
