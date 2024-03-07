class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)
        for i in range(min_length):
            if len(set(s[i] for s in strs)) != 1:
                return strs[0][:i]
        
        return strs[0][:min_length]

# Пример использования:
solution = Solution()

strs1 = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(solution.longestCommonPrefix(strs2))  # Output: ""
