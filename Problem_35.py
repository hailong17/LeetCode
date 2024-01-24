import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for number in nums:
            if number == target:
                index = nums.index(number)
                return index

if __name__ == '__main__':
    solution = Solution()
    solution.searchInsert()