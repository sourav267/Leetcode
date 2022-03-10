# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumI = l1.val + l2.val
        digit, tenth = sumI % 10,sumI // 10
        answer = ListNode(digit)
        if l1.next or l2.next or tenth > 0:
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += tenth
            answer.next = self.addTwoNumbers(l1, l2)    
        return answer
        
#         answer = root = ListNode(0)
#         carry = 0
        
#         while l1 or l2 or carry > 0:
#             sumI = l1.val + l2.val + carry
#             answer.next, carry = ListNode(sumI % 10) , sumI//10
#             l1=l1.next
#             l2=l2.next
#             answer = answer.next
            
#         return root.next
        
            