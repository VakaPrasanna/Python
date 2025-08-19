#314
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]

Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
================================================================================================================================
from collections import deque, defaultdict

class TreeNode:
    def __init__(self,val):
        self.val=int(val)
        self.left=None
        self.right=None

def build_tree(values):
    if not values or values[0]=="null":
        return None
    
    root=TreeNode(values[0])
    queue=deque([root])
    i=1
    
    while queue and i<len(values):
        node=queue.popleft()
        
        if i<len(values) and values[i]!="null":
            node.left=TreeNode(values[i])
            queue.append(node.left)
        i+=1
        
        if i<len(values) and values[i]!="null":
            node.right=TreeNode(values[i])
            queue.append(node.right)
        i+=1
    return root
    

def vertical_traversal(root):
    if not root:
        return []
    col_table=defaultdict(list)
    queue=deque([(root,0)])
    
    while queue:
        node,col=queue.popleft()
        col_table[col].append(node.val)
        
        if node.left:
            queue.append((node.left,col-1))
        if node.right:
            queue.append((node.right,col+1))
    res=[col_table[x] for x in sorted(col_table.keys())]
    return res

if __name__=="__main__":
    vals=input("Enter space-separated values (null for empty): ").strip().split()
    root=build_tree(vals)
    result=vertical_traversal(root)
    print("Result: ", result)

Enter space-separated values (null for empty): 3 9 8 4 0 1 7 null null null 2 5
Result:  [[4], [9, 5], [3, 0, 1], [8, 2], [7]]

