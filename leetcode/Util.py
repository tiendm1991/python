# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createListNode(arr):
    if arr == None or len(arr) == 0:
        return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        newNode = ListNode(arr[i])
        cur.next = newNode
        cur = newNode
    return head


def createTree(arr):
    if arr == None or len(arr) == 0:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        while queue[0] == None:
            del queue[0]
        left, right = None, None
        if arr[i] != None:
            left = TreeNode(arr[i])
        queue[0].left = left
        queue.append(left)
        i += 1
        if i == len(arr):
            break
        if arr[i] != None:
            right = TreeNode(arr[i])
        queue[0].right = right
        queue.append(right)
        i += 1
        del queue[0]
    return root
