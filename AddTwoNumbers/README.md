TwoSum
=======
>You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

>You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

This has a difficulty medium problem from [LeetCode](https://leetcode.com/problems/add-two-numbers/). Since the format used is a LinkedList, I decided to use a recursive approach to the problem. LinkedLists are a recursive data structure and it is cleaner to handle recursive data structures with recurisve code.

Base Cases: LinkedList.vals are None

Recursive Code: Add the sum of each LinkedList.val to a new LinkedList

[Original Code](AddTwoNumbers-Orig.py): Runtime = O(n)

```python
class Solution():

    def addTwoNumbersHelper(self, n1 , n2,tenths=0):
        #Base Cases
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
        #Recursive Code
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
``` 

[Optimized Solution](AddTwoNumbers.py): Runtime = O(n)
```python
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
         #Base Cases
        if n1 is None:
            if n2 is None:
                if has_carry:
                    return ListNode(1)
                else:
                    return None
            n1 = ListNode(0)
        elif n2 is None:
            n2 = ListNode(0)
        #Recursive Code
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
```

Lessons Learned
---------------------

After completing the AddTwoNumbers code with solution, Through the comments I learned that that Subtraction is faster than Division. In a general sense subtraction is easier than division and my guess is that the computer handles it very similarly. When you also consider floating point values which are stored in a completely different format than integers it would not be hard to say subtraction is indeed faster than division. 

*See [Tests.py](Tests.py)*

Lastly for some reason, when I first submitted by code I had learned that functions within classes require the self variable so that it can be called. I haven't done much OOD in Python so this is something new to me :)
