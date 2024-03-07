# strs = ["flower", "flow", "flight"]
strs = ["dog", "racecar", "car"]
strs = []
strs = ["dog", "dog", "dog",]
def common_prefix(strs):
    
    if not strs:
        return ""
    
    min_length = min(len(s) for s in strs)

    for i in range(min_length):
        a = set((s[i] for s in strs))
        if len(a) != 1:
            return(strs[0][:i])

    return strs[0]

# min_length = min(len(s) for s in strs)
# for i in range(min_length):
#     if len(set(s[i] for s in strs)) != 1:
#         return strs[0][:i]

# return strs[0][:min_length]

print(common_prefix(strs))