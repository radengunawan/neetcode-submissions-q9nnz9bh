class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i:[] for i in range (numCourses)}

        for course, preq in prerequisites:
            adj[course].append(preq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adj[course] == []:
                return True
            
            visited.add(course)
            for preq in adj[course]:
                if not dfs(preq):
                    return False
            
            visited.remove(course)
            adj[course] = []

            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

        