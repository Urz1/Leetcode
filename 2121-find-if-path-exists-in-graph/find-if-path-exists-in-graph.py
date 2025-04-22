class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination :
            return True
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        flag = False
        visited = set()
        def dfs(vertex,visited):
            nonlocal flag
            if vertex == destination:
                flag = True
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    dfs(neighbour, visited)
        for edge in edges:
            if edge[0] == source:
                dfs(edge[0],visited)
                return flag
            elif edge[1] == source:
                dfs(edge[1],visited)
                return flag
        