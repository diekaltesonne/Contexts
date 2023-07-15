# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _reverseList(self, head, _prev):
        if head is not None:
            n_head = head.next
            head.next = _prev
            if n_head is None:
                return head
            return self._reverseList(n_head,head)  
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self._reverseList(head,None)
        ans = []
        # while head is not None:
        #     ans.append(head.val)
        #     head = head.next
        return head
        