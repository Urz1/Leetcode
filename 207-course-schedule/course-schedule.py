class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        '''
        using coloring 
        assume white as 0
        gray as 1
        black as 2
        *** if we got at a point where we have visited it's childrens and it's color is gray 
        this means we have got a cycle 
        '''
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)

        colors = [0 for course in range(numCourses)]
        def dfs(course):
            if colors[course] == 1:
                return False

            if colors[course] == 2:
                return True
            colors[course] = 1

            for child in graph[course]:
                if not dfs(child):
                    return False
            colors[course] = 2

            return True
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


        # visited = defaultdict(int)
        # def dfs(vertex, visited):
        #     if visited[vertex] == 1:
        #         return False
        #     visited[vertex] = visited.get(vertex, 0) + 1
        #     for neighbour in graph[vertex]:
        #         if neighbour not in visited:
        #             dfs(neighbour, visited)
        # graph = defaultdict(list)
        # for course in prerequisites:
        #     graph[course[0]].append(course[1])
        #     # graph[course[1]].append(course[0])
        # for course in prerequisites:
        #     if visited[course[0]] != 2:
        #         dfs(course[1],visited) 
        # return True