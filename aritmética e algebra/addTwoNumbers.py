# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value1 = ""
        current = l1
        while True:
            value1 += str(current.val)
            current = current.next
            if current == None:
                break

        value2 = ""
        current = l2
        while True:
            value2 += str(current.val)
            current = current.next
            if current == None:
                break


        lista = ListNode()
        
        current = lista
        value1 = int(value1[::-1])
        value2 = int(value2[::-1])
        res = value1 + value2
        res = str(res)[::-1]
        
        for index, i in enumerate(res):
            print(current.val)
            current.val = int(i)
            if index < len(res)-1:
                current.next = ListNode()
                current = current.next

        return lista
