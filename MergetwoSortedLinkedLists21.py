Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
-------------------------------------------------
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def build_ll(nums):
    dummy=ListNode()
    curr=dummy
    for n in nums:
        curr.next=ListNode(n)
        curr=curr.next
    return dummy.next
    
def print_list(head):
    while head:
        print(head.val, end=' ')
        head=head.next
    print()
    
def merge_sorted_lists(lst1,lst2):
    dummy=ListNode()
    curr=dummy
    
    if not lst1:
        return lst2
        
    if not lst2:
        return lst1
        
    while lst1 and lst2:
        if lst1.val < lst2.val:
            curr.next=lst1
            lst1=lst1.next
        else:
            curr.next=lst2
            lst2=lst2.next
        curr=curr.next
        
    curr.next=lst1 if lst1 else lst2
    return dummy.next
            
    
l1=list(map(int, input("Enter list1: ").split()))
l2=list(map(int, input("Enter list2: ").split()))
ll1=build_ll(l1)
ll2=build_ll(l2)
ml=merge_sorted_lists(ll1,ll2)
print_list(ml)

---------------------------------------
Enter list1: 1 3 4
Enter list2: 1 2 4
1 1 2 3 4 4 
