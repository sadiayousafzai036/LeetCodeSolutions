# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        sum = 0
        if root is None:
            return 0

        if root.val >= L and root.val <= R:
            sum += root.val
            sum += self.rangeSumBST(root.left, L, R)
            sum += self.rangeSumBST(root.right, L, R)
        elif root.val < L:
            sum += self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            sum += self.rangeSumBST(root.left, L, R)
        return sum
