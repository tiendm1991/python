class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        def buildTree(l, r):
            result = []
            if l > r:
                return [None]
            for x in range(l, r + 1):
                left = buildTree(l, x - 1)
                right = buildTree(x + 1, r)
                for le in left:
                    for ri in right:
                        result.append(TreeNode(x, le, ri))
            return result

        return buildTree(1, n)
