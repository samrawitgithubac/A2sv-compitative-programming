# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insertion(root):
             
            if root==None:
                return None
                
            if root.val==val:
                return root
            if root.val>val:
                return insertion(root.left)
                
            if root.val<val:
                return insertion(root.right)
            
        return insertion(root)
           

        
        