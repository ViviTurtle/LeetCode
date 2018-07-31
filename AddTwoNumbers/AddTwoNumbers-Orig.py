import ListNode

class Solution():

    def addTwoNumbersHelper(self, n1 , n2,tenths=0):
        if n1 is None:
            if n2 is None:
                if tenths != 0:
                    currentNode = ListNode(tenths)
                    return currentNode
                else:
                    return None
            else:
                n1 = ListNode(0)
        elif n2 is None:
            n2 = ListNode(0)
        total = n1.val + n2.val + tenths
        tenths = total//10
        currentNode = ListNode(total % 10)
        currentNode.next = self.addTwoNumbersHelper(n1.next, n2.next, tenths)
        return currentNode


    def addTwoNumbers(self, l1, l2):
        global currentNode
        if None in (l1, l2):
            currentNode = ListNode(None, None)
        else:
            currentNode = self.addTwoNumbersHelper(l1, l2)
        return currentNode