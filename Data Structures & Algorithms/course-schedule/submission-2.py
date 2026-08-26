class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqNum = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            prereqNum[crs] += 1
            adj[pre].append(crs)

        q = deque()
        for n in range(numCourses):
            if prereqNum[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nextCRS in adj[node]:
                prereqNum[nextCRS] -= 1
                if prereqNum[nextCRS] == 0:
                    q.append(nextCRS)

        return finish == numCourses


        