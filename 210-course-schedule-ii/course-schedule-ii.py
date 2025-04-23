class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)     
            indegree[course] += 1         

        queue = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return ans if len(ans) == numCourses else []