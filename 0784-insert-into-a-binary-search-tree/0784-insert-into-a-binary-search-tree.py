# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insertion(root,curr):
            if  root is None:
                return TreeNode(curr)
            if root.val<curr:
                root.right= insertion(root.right,curr)
                return root

            if root.val>curr:
                root.left= insertion(root.left,curr)
                return root
        return insertion(root,val)
            
               


           
            