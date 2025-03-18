# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symetrical(obj,img):
            if  not obj and not img:
                return True
            if (obj and not img ) or  (img and not obj):
                return False

            if obj.val!=img.val:
                return False
            else:
                return  symetrical(obj.right,img.left) and  symetrical(obj.left,img.right)

        return symetrical(root,root)