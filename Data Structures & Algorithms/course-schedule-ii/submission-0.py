class Solution:
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:
        deg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        q = deque()

        for (a, b) in prereqs:
            deg[a] += 1
            adj[b].append(a)
        for c in range(numCourses):
            if deg[c] == 0:
                q.append(c)
        course_order = []
        while q:
            a = q.pop()
            course_order.append(a)
            for b in adj[a]:
                deg[b] -= 1
                if not deg[b]:
                    q.append(b)

        if len(course_order) == numCourses:
            return course_order
        return []
        