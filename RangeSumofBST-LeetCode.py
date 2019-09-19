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
        else:
            if root.val >= L and root.val <= R:
                sum += root.val
            if root.val > L:
                self.rangeSumBST(root.left, L, R)
            if root.val < R:
                self.rangeSumBST(root.right, L, R)
        return sum


ts=Solution()
#print(ts.rangeSumBST([10,5,15,3,7,None,18],7,15))

print(ts.rangeSumBST([10,5,15,3,7,13,18,1,None,6],6,10))