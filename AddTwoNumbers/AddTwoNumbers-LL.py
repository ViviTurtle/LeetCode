# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import ListNode

class Solution():

    def addTwoNumbersHelper(self, n1 , n2, has_carry=0):
        """
        Recursive Helper used to add two ListNode of Numbers.
        Note: Subtract is used over Division since Subtraction has a faster runtime than subtraction
              See https://stackoverflow.com/questions/1396564/why-is-subtraction-faster-than-addition-in-python
              This is also useful because the carry will NEVER be more than one
        :param n1: First set of Numbers to add
        :param n2: Second set of Numbers to add
        :param has_carry: Boolean value if numbers are carried
        :return: Resulting ListNode
        """
        if n1 is None:
            if n2 is None:
                if has_carry:
                    return ListNode(1)
                else:
                    return None
            n1 = ListNode(0)
        elif n2 is None:
            n2 = ListNode(0)
        total = n1.val + n2.val + has_carry
        if total > 9:
            has_carry = 1
            total -= 10
        else:
            has_carry = 0
        currentNode = ListNode(total)
        currentNode.next = self.addTwoNumbersHelper(n1.next, n2.next, has_carry)
        return currentNode


    def addTwoNumbers(self, l1, l2):
        return self.addTwoNumbersHelper(l1, l2)