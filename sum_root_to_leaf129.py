129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026

Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

---------------------------------------------------------------
class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
def sum_root_to_leaf(root):
    def dfs(node, curr_num):
        if not node:
            return 0
        curr_num=(curr_num*10)+node.val
        if not node.left and not node.right:
            return curr_num
        return dfs(node.left,curr_num)+dfs(node.right,curr_num)
    return dfs(root,0)

root=TreeNode(4)
root.left=TreeNode(9)
root.right=TreeNode(0)
root.left.left=TreeNode(5)
root.left.right=TreeNode(1)
res=sum_root_to_leaf(root)
print(res)


