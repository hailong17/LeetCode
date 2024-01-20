# 217. Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.
import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False

    def solution2(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i+1]:
                return True
        return False