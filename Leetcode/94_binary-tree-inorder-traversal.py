# [Tree Traversals (Inorder, Preorder and Postorder)](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/)
# [How to implement Inorder traversal in a binary search tree?](https://dev.to/javinpaul/how-to-implement-inorder-traversal-in-a-binary-search-tree-1787#:~:text=The%20InOrder%20traversal%20is%20one,nodes%20on%20the%20right%20subtree.)
# Definition for a binary tree node.

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        pass

def main():
    a = Solution()
    root = [1,None,2,3]
    a.inorderTraversal(root)
    print(root)

if __name__ == "__main__":
    main()