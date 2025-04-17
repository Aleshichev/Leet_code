class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n_2 = s.strip()[::-1]
        len_world = 0
        for char in n_2:
            if char != ' ':
                len_world +=1
            else: break

        return len_world
                    
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         pointer = len(s) -1
#         lenght = 0
        
#         while s[pointer] == " ":
#             pointer -= 1
#         while pointer >= 0 and s[pointer] != " ":
#             pointer -= 1
#             lenght +=1
        
#         return lenght
        
        
s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("a"))