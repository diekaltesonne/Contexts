# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = 0
        b = 0
        for i in range (l1):
            for j in l2:
                if j >= l1[i]:
                    a = i
                    b = j
                else:
                    c = l1[i].next 
                    l1[i].next = j
                    l1[i].next.next = c
        return l1            