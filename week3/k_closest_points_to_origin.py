class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_p = {}
        for p in points:
            if p[0]**2 + p[1]**2 in dist_p:
                dist_p[p[0]**2 + p[1]**2].append(p)
            else:
                dist_p[p[0]**2 + p[1]**2] = [p]
        mins = sorted(dist_p.keys())
        output = []
        while len(output) < k:
            output.append(dist_p[mins[0]].pop())
            if len(dist_p[mins[0]]) == 0:
                mins.pop(0)
        return output
