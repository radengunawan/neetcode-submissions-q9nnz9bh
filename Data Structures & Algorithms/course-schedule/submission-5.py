class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courseMap = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            courseMap[course].append(prereq)

        visited = set()

        def dfs(current_course):
            if courseMap[current_course] == []:
                return True
            if current_course in visited:
                return False
            
            visited.add(current_course)
            for prereq in courseMap[current_course]:
                if not dfs(prereq):
                    return False

            courseMap[current_course] = []
            visited.remove(current_course)

            return True
            
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        