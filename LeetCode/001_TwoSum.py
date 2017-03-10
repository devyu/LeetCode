#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def twoSum(self, nums, target):
        for k, v in enumerate(nums):
            ret = target - nums[k]
            index = nums.index(ret)
            if ret in nums and index != k:
                return [k, index]

if __name__ == "__main__":
    s = Solution()
    l = s.twoSum([3,2,4], 6)
    print(l)
