class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build a graph with the courses as nodes, directed edge from course to prereq
        prereqs = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        # detecting cycles in a directed graph through dfs
        visited = set()

        def dfs(course):
            if prereqs[course] == []:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            prereqs[course] = []
            return True
        
        return all(dfs(c) for c in range(numCourses))
