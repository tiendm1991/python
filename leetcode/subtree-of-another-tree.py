from  datetime import datetime

from leetcode.Util import TreeNode
from leetcode import Util

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSub(source, target):
            if source == None :
                return target == None
            if target == None:
                return source == None
            if source.val != target.val:
                return False
            return isSub(source.left, target.left) and isSub(source.right, target.right)

        def traversal(source):
            if source == None:
                return False
            if isSub(source, t):
                return True
            return traversal(source.left) or traversal(source.right)
        return traversal(s)

s = Solution()
startTime = datetime.now()
print(s.isSubtree(Util.createTree([3,4,5,1,None,2]), Util.createTree([3,1,2])))
print(datetime.now() - startTime)