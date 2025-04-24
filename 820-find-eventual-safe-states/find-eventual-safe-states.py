class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        alist = defaultdict(list)         
        reverse = defaultdict(list)      

        for i in range(n):
            alist[i] = graph[i]
            for nei in graph[i]:
                reverse[nei].append(i)    

        queue = deque()
        order = []
        for i in range(n):
            if not alist[i]:
                queue.append(i)
                order.append(i)

        visited = [False] * n
        for i in order:
            visited[i] = True

        while queue:
            course = queue.popleft()
            for parent in reverse[course]:   
                if course in alist[parent]:
                    alist[parent].remove(course)
                    if not alist[parent] and not visited[parent]:
                        queue.append(parent)
                        order.append(parent)
                        visited[parent] = True

        return sorted(order)