# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        if head.next ==None :
            return head

        dummiHead = ListNode()
        dummiHead.next = head
        runner = head
        counter = head
        count = 1
        while counter.next:
            counter= counter.next
            count +=1
            
        if k > count:
            k = k%count
        print(count)  
        print(k)

        for i in range(k):
            while runner.next.next:
                runner= runner.next

            lastNode = runner.next
            runner.next = None
            lastNode.next= dummiHead.next
            dummiHead.next = lastNode
            runner = lastNode
        
        return dummiHead.next