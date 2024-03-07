class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_dict = {}
        for i, num in enumerate(nums):
            new_num = target - num
            if num in new_dict:
                return[new_dict[num], i]
            new_dict[new_num]= i




solution = Solution()  
      
# nums = [7,11,15,2] 
# target = 9 # Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# nums = [3,2,4]
# target = 6 # Output: [1,2]

nums = [2,1,3,1,3,4,5,6,7,8,4]
target = 6 # Output: [0,1]

print(solution.twoSum(nums, target))
 
