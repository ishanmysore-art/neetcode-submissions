class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build a graph where the nodes are the courses and
        # there is a directed edge from each node to the prerequisite
        visited = set()

        prereqs = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        # check cycle detection -- if cycle detected, then return false
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
            

        return all(dfs(i) for i in range(numCourses))
