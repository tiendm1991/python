class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        if leftChild[0] == -1 and rightChild[0] == -1:
            return False
        for x in leftChild:
            if x != -1 and x in rightChild:
                return False
        parent = {}
        for i in range(len(leftChild)):
            if leftChild[i] == -1:
                continue
            if i in parent and parent[i] == leftChild[i]:
                return False
            parent[leftChild[i]] = i
        parent = {}
        for i in range(len(rightChild)):
            if rightChild[i] == -1:
                continue
            if rightChild[i] in parent and parent[rightChild[i]] == i:
                return False
            parent[rightChild[i]] = i
        tree = set()
        stack = [0]
        while len(stack) > 0:
            par = stack.pop()
            tree.add(par)
            if rightChild[par] != -1:
                stack.append(rightChild[par])
            if leftChild[par] != -1:
                stack.append(leftChild[par])
        return len(tree) == n


s = Solution()
print(s.validateBinaryTreeNodes(6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1]))