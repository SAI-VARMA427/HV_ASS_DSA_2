# Question 1 - 

# Write a program to create a function that takes two sorted linked lists in ascending order as input and returns a sorted linked list in ascending order. 

# Input:
#       list1= 2->1->3
#       list2=4->6->5

# Output :  sortedlist = 1->2->3->4->5->6

# Note - Don’t use any in-built functions

class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next