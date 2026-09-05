class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i:[] for i in range(numCourses)}

        howManyDependOnMe = {i:0 for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[course].append(prereq)
            howManyDependOnMe[prereq] +=1
        
        q = deque()
        
        for course in range(numCourses):
            if howManyDependOnMe[course] == 0:
                q.append(course)
        
        course_completed = 0

        while q:
            current_course = q.popleft()
            course_completed +=1
            for neigh in adj[current_course]:
                howManyDependOnMe[neigh] -= 1
                if howManyDependOnMe[neigh] == 0:
                    q.append(neigh)
        
        return course_completed == numCourses
        