class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {x : True for x in range(numCourses)}
        adj = {}
        pre = {}
        taken = set()
        s = []
        for c1, c2 in prerequisites:
            if c2 not in adj:
                adj[c2] = []
            adj[c2].append(c1)
            if c1 not in pre:
                pre[c1] = []
            pre[c1].append(c2)
            if c1 in d:
                del d[c1]
        
        for course in d:
            s.append(course)
            taken.add(course)
        while s:
            course = s.pop()
            if course in adj:
                for nex in adj[course]:
                    if nex not in taken:
                        pre[nex].remove(course)
                        if not pre[nex]:
                            taken.add(nex)
                            s.append(nex)
        return len(taken) == numCourses
