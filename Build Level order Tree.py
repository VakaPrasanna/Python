from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=int(val)
        self.left=None
        self.right=None
        


#Build Tree from level-order input
def build_tree(values):
    if not values or values[0]=="null":
        return None
    
    root=TreeNode(values[0])
    queue=deque([root])
    i=1
    
    while queue and i<len(values):
        node=queue.popleft()
        
        #left child
        if i<len(values) and values[i]!="null":
            node.left=TreeNode(values[i])
            queue.append(node.left)
        i+=1
        
        #Right child
        if i<len(values) and values[i]!="null":
            node.right=TreeNode(values[i])
            queue.append(node.right)
        i+=1
    return root
    
    
#input values
if __name__=="__main__":
    vals=input("Enter space-separated values (null for empty): ").strip().split()
    root=build_tree(vals)
    #result=vertical_traversal(root)
    print("values: ",vals)
    print(f"Result: {root.val}")
    



