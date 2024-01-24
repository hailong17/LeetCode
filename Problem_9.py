class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return string == string[::-1]
if __name__ == '__main__':
    solution = Solution()
    solution.isPalindrome(121)