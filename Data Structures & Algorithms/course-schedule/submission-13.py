class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i:[] for i in range(numCourses)}
        preqNeededBy = [0]*numCourses

        for course, preq in prerequisites:
            adj[course].append(preq)
            preqNeededBy[preq]+=1
        
        q = deque()
        for i in range(numCourses):
            if preqNeededBy[i] == 0:
                q.append(i)
        
        courseFinished = 0

        while q:
            currentCourse = q.popleft()
            courseFinished +=1

            for preq in adj[currentCourse]:
                preqNeededBy[preq] -= 1
                if preqNeededBy[preq] == 0:
                    q.append(preq)
        
        return courseFinished == numCourses
                