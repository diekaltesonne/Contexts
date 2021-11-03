"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#write your code here
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            mapping[node] = Node(node.val)
            for i in node.neighbors:
                if i not in mapping:
                    dfs(i)
                mapping[node].neighbors += [mapping[i]]
        if not node: return node
        mapping = {}
        dfs(node)
        return mapping[node]
