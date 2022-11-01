class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        directions = [0, 1, 0, -1, 0]
        toFlood = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    toFlood.append((i, j))
                else:
                    mat[i][j] = -1
        
        while toFlood:
            r, c = toFlood.popleft()
            for i in range(4):
                neighbor_r = directions[i] + r
                neighbor_c = directions[i + 1] + c
                if m > neighbor_r >= 0 and n > neighbor_c >= 0 and mat[neighbor_r][neighbor_c] == -1:
                    mat[neighbor_r][neighbor_c] = mat[r][c] + 1
                    toFlood.append((neighbor_r, neighbor_c))
        return mat
                
