class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        deg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        q = deque()

        for (a, b) in prereqs:
            deg[b] += 1
            adj[a].append(b)
        for c in range(numCourses):
            if deg[c] == 0:
                q.append(c)
        course_count = 0
        while q:
            a = q.pop()
            course_count += 1
            for b in adj[a]:
                deg[b] -= 1
                if not deg[b]:
                    q.append(b)

        if course_count == numCourses:
            return True
        return False


        