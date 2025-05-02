class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        flag = True
        graph  = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        visited = set()
        colors = [0] * numCourses
        def dfs(node):
            nonlocal flag
            if not flag:
                return
            colors[node] = 1
            for neighbor in graph[node]:
                if colors[neighbor] == 1:
                    flag = False 
                    return
                if colors[neighbor] == 0:
                    dfs(neighbor)
            colors[node] = 2
        for course in range(numCourses):
            if colors[course] == 0:
                dfs(course)
        return flag
