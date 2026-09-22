# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        visited = set()
        current = head

        while current.next:
            visited.add(current)
            current = current.next
            if (current.next in visited):
                return True
        return False


        