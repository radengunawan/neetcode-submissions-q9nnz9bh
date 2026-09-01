class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        coursesDependOnMe = [0]*numCourses
        adj = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[course].append(prereq)
            coursesDependOnMe[prereq] +=1

        q = deque()
        
        for i in range(numCourses):
            if coursesDependOnMe[i] == 0:
                q.append(i)
        
        finishedCourse = 0

        while q:
            current_node = q.popleft()
            finishedCourse +=1
            for nei in adj[current_node]:
                coursesDependOnMe[nei] -=1
                if coursesDependOnMe[nei] == 0:
                    q.append(nei)
        
        return finishedCourse == numCourses

        