TwoSum
=======
>Given an array of integers, return indices of the two numbers such that they add up to a specific target.

>You may assume that each input would have exactly one solution, and you may not use the same element twice.

>Example:
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
This is the very first [problem](https://leetcode.com/problems/two-sum/) given to us at [LeetCode](https://leetcode.com/). Some solutions are already provided in Java but I attempted to write the code in python.

[Original Code](twoSum-Orig.py): Runtime = O(n)

```python
class Solution:
    def twoSum(self, nums, target):
      #initiate dictionary
      lookup_set = {}
      length = len(nums)
      #for loop
      for i in range (0, length):
        curr_value  = nums[i]
        complement = target - curr_value
        #in dict is O(1) access
        if complement in lookup_set:
          return [lookup_set[complement],i]
        lookup_set[curr_value] = i
``` 

[Optimized Solution](twoSum-LL.py): Runtime = O(n)
```python
class Solution:
    def twoSum(self, nums, target):
      lookup_set = {}
      for i, curr_value in enumerate(nums):
        complement = target - curr_value
        if complement in lookup_set:
          return [lookup_set[complement],i]
        lookup_set[curr_value] = i
```

Lessons Learned
---------------------

After completing the twoSum code with my semi-optimized solution, I viewed the other way people solved the problem. This led me to the method **enumerate()**. This method iterates through a list and returns a tuple - (index,value). This is very useful when you want to make a **for each** loops where you will be using the value **and** the index. tldr; - You can turn the following loop:

```python
 for index in range (0, length):
        curr_value  = nums[i]
        ...
```

into:
```python
for index, curr_value in enumerate(nums):
```

This is best practice in order to make python code more **pythonic** - As in more readable code where you don't have to keep track of indexes and values. 
