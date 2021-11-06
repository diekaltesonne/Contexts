# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def _deleteDuplicates(self,head,a,pointer):
    if head.next is None:
        return 0
    else:
        if head.val == head.next.val:
            a = head.val
            return self._deleteDuplicates(head.next,a,pointer)
        else:
            if a == head.val:
                #if head.next.next is not None:
                #    if pointer.next.val == head.next.next.val:
                #       return self._deleteDuplicates(head.next,a,pointer)
                #    return self._deleteDuplicates(head.next,a,pointer)
                #else:
                #    pass
                #pointer.next = head.next
                return self._deleteDuplicates(head.next,a,pointer)
            else:
                pointer.next = head
                return self._deleteDuplicates(head.next,a,head)
        
def _deleteDuplicates_2(self,head,pointer):
    a = 0
    c = None
    while head.next is not None:
        if head.val == head.next.val:
            a = head.val 
        else:
            if a == head.val:
                if pointer.val != a:
                    pointer.next = head.next
                    c = pointer
                    pointer = head.next
                else:
                    c.next = head.next
                    c = head.next
                    pass
            else:
                pointer.next = head
                pointer = head
        head = head.next

def _deleteDuplicates_3(self,head,pointer_a,pointer):
    a = 0
    head_main = head
    while head.next is not None:
        if head.val == head.next.val:
            a = head.val 
        else:
            if a == head.val:
                if pointer_a.val != a:
                    pointer.next = head.next
                    pointer_a = pointer
                else:
                    pointer_a.next = head.next
            else:
                pointer.next = head
                pointer = head
        head = head.next
    return head_main

class Solution:
    def _deleteDuplicates_4(self,head):
        if head is None:
            return head
        a = 0
        list_of_nodes = []
        while head is not None:
            if head.next is not None and head.val == head.next.val:
                a = head.val
                if len(list_of_nodes) != 0\
                    and list_of_nodes[-1].val == head.next.val:
                    print(list_of_nodes.pop().val)
            else:
                if a == head.val:
                    if head.next is not None:
                        list_of_nodes.append(head.next)
                else:
                    list_of_nodes.append(head)
            head = head.next

        print(list_of_nodes)

        if len(list_of_nodes) != 0:
            if list_of_nodes != [None]:
                for i in range(len(list_of_nodes)):
                    if i < len(list_of_nodes) - 1:
                        list_of_nodes[i].next = list_of_nodes[i+1]
                    else:
                        list_of_nodes[i].next = None
                return list_of_nodes[0]
        else:
            return None


    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._deleteDuplicates_4(head)