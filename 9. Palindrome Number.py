class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
    
solution = Solution()  

x = 121
# x = -121
# x = 10
print(solution.isPalindrome(x))