# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        to_delete = set(nums)  
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            if curr.val in to_delete:
                prev.next = curr.next  
            else:
                prev = curr
            curr = curr.next

        return dummy.next