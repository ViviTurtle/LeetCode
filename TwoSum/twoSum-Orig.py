class Solution:
    def twoSum(self, nums, target):
      lookup_set = {}
      length = len(nums)
      for i in range (0, length):
        curr_value  = nums[i]
        complement = target - curr_value
        if complement in lookup_set:
          return [lookup_set[complement],i]
        lookup_set[curr_value] = i