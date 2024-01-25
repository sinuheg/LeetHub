"""
visited = [0 1 2 5, 6, 4, 3]
stack = [3]
path = [0 1 2 4 3 1]

node = 1
prev = 3
"""
from collections import deque
class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacency = {}
        for node in range(n):
            adjacency[node] = []
        for node1,node2 in edges:
            adjacency[node1].append(node2)
            adjacency[node2].append(node1)
        visited = set()
        cycle = set()
        stack = [(0,None)]
        path = []
        while stack:
            node, prev = stack.pop()
            while path and path[-1] != prev:
                    path.pop()
            if node in visited:
                cycle.add(node)
                while path and path[-1] != node:
                    cycle.add(path.pop())
                break
            else:
                visited.add(node)
                path.append(node)
                for child in adjacency[node]:
                    if child != prev:
                        stack.append((child,node))
        def bfs(initial_node):
            q = deque()
            q.append((initial_node,0))
            while q:
                node, distance = q.popleft()
                distances[node] = min(distances[node], distance)
                if node in visited:
                    continue
                visited.add(node)
                for child in adjacency[node]:
                    if child not in cycle:
                        q.append((child, distance+1))
        distances = [99999999] * n
        print(len(cycle))
        for node in list(cycle):
            visited = set()
            bfs(node)
        return distances 


        