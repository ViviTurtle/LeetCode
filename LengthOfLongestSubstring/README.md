Length of Longest Substring Without Repeating Characters
=======
>Given a string, find the length of the longest substring without repeating characters.

>Example:
```
Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

This is a difficulty medium problem from [LeetCode](https://leetcode.com/problems/add-two-numbers/). At first I thought this would be fairly simple. My initial algorithm being:

1) Iterate each character from start of substring
    1) Record Start of Substring
    2) Record Last Character Added (In a dictionary)
2) When Last Character is repeated:
    1) Record Length since of substring
3) Increase Start of Substring by 1 and Repeat

At first I thought this was pseudocode was great. It uses a dictionary to reduce access to characters seen and it seems to cover all the bases. I only later realized this algorithm has a runtime of O(n^2) and was very messy.  Additionally, for some random reason, I assumed a repeated character would repeat due to a character found in the **beginning** of the substring


[Original Code](ALengthOfLongestSubstring-Orig.py): Runtime = O(n^2)

```python
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        current_length = 0
        iterator = 1
        current_characters = dict()
        start_position = 0
        while iterator <= len(s):
            current_char = s[iterator-1:iterator]
            if current_characters.get(current_char) is None:
                current_length = current_length + 1
                current_characters[current_char] = iterator
                iterator += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                iterator = current_characters.get(current_char) + 1
                current_characters.clear()
                current_length = 0
        if current_length > max_length:
            max_length = current_length
        return max_length
``` 

[Optimized Solution](LengthOfLongestSubstring-LL.py): Runtime = O(n)
```python
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        current_characters = dict()
        start_position = 0
        print s
        for iterator, character in enumerate(s, 1):
            #If character in dictionary Or while loop is exiting
            if current_characters.get(character) and current_characters.get(character) > start_position:
                    start_position = current_characters.get(character)
            current_length = iterator - start_position
            if current_length > max_length:
                max_length = current_length
            current_characters[character] = iterator
        return max_length
```

So what changed? I was able to change the algorithm to use a single *for* loop without reiterating already added characters. 
1) Instead of increasing the *start_position* by one and repeating, I stored/retrieved the index of the repeated character and set that as the new starting point. 
2) I did not clear the *seen characters* dictionary, and simply checked to see if its position is greater than the starting point. This let me not have to reiterate back to the starting position


Lessons Learned
---------------------

There are quite a few things I learned on this one. 
1) **enumerate** indices can be set to iterate starting from an integer of your choice
2) Using the Max built-in function is **only** faster than a manual **if curr>max:** statement if your iterating over a list. If you are calling max within a **for** loop it is significantly slower. 
    1) *See [Tests.py](Tests.py)* and  [LengthOfLongestSubstring-Max](LengthOfLongestSubstring-Max.py)*
3) *None*, *Empty*, *0*, and *False* evaluate to False if used in a conditional. As in, if a variable is not set, that variable will evaluate to None, and thus the resulting conditional will result to *False*
    1)  See Below:
        ```python
        a = "hello"
        b = ""
        c = None
        def testBoolean(s):
            if s:
                 print "True"
            else:
                 print "False"
        
        #Testing
        testBoolean(a)
        >>> True
        testBoolean(b)
        >>> False
        testBoolean(c)
        >>> False
        
        d = dict()
        d["test"] = True
        
        #Dictionary Testing
        d.get("test")
        >>> True
        testBoolean(d)
        >>> True
        testBoolean(d.get("test"))
        >>> True
        testBoolean(d.get("rawr"))
        >>> False
         ```
4) I need to manually run through an algorithm before I actually start programming. I need to not rush, and grab all edge cases.
5) Lastly, I re-learned (Since my programming in Java days), that one-off issues are still a huge pain.
