"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = dict()

        def dfs(curr):
            if not curr:
                return None
            if curr in node_map:
                return node_map[curr]
            
            node_map[curr] = Node(val=curr.val)
            
            for n in curr.neighbors:
                node_map[curr].neighbors.append(dfs(n))

            return node_map[curr]

        return dfs(node)
