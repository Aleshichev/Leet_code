class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for haystack_index in range(len(haystack) - len(needle) + 1):
            for needle_index in range(len(needle)):
                if haystack[haystack_index + needle_index] != needle[needle_index]:
                    break
                if needle_index == len(needle) -1:
                    return haystack_index
        return -1
                    
   
        
        
        
        
s = Solution()
print(s.strStr("khig8sadbuts2ad","sad"))