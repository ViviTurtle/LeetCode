class Solution:
    def twoSum(self, nums, target):
      lookup_set = {}
      for i, curr_value in enumerate(nums):
        complement = target - curr_value
        if complement in lookup_set:
          return [lookup_set[complement],i]
        lookup_set[curr_value] = i