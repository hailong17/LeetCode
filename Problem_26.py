
class Solution:
    def removeDuplicates(nums):
        list_num = []
        for num in nums:
            if num not in list_num:
                list_num.append(num)
        
        for i in range(len(list_num), len(nums)):
            list_num.append('_')

        return list_num

if __name__ == '__main__':
    list_num = [1,1,2]
    Solution.removeDuplicates(list_num)