class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]
        courseNext = [0]*numCourses

        for course, pre in prerequisites:
            adj[course].append(pre)
            courseNext[pre]+=1
        
        q = deque()
        visited = set()

        for i in range (numCourses):
            if courseNext[i] == 0:
                q.append(i)
                visited.add(i)
        
        finishedCourse = 0

        while q:
            current_course = q.popleft()
            finishedCourse +=1

            for preq in adj[current_course]:
                courseNext[preq] -=1
                if courseNext[preq] == 0:
                    q.append(preq)
                    
        
        return finishedCourse == numCourses

        

        

        