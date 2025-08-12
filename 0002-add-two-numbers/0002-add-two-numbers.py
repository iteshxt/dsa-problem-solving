# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()   # temporary starting point
        current_node = temp
        carry_over = 0
        
        while l1 or l2 or carry_over:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            
            total_sum = digit1 + digit2 + carry_over
            carry_over = total_sum // 10
            new_digit = total_sum % 10
            
            current_node.next = ListNode(new_digit)
            current_node = current_node.next
            
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next
        
        return temp.next