# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return str(self.val) + '|' + '.'.join([str(neighbor.val) for neighbor in self.neighbors])


class Solution:
    def cloneGraph(self, root: Node) -> 'Node':
        m = {}

        def dfs(node: Node):
            if not node:
                return node
            newNode = Node(node.val)
            m[node] = newNode
            newNode.neighbors = []
            for ne in node.neighbors:
                if ne in m:
                    newNode.neighbors.append(m[ne])
                else:
                    newNode.neighbors.append(dfs(ne))
            return newNode

        return dfs(root)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

s = Solution()
print(s.cloneGraph(n1))
