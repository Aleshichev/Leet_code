from typing import List

class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # print(id(nums1))
        # # nums1 = nums1[:m]
        # for _ in range(m):
        #     nums1.pop()
        # print(id(nums1))
        # nums2 = nums2[:n]
        # nums1.extend(nums2)
        # print(id(nums1))
        # nums1.sort()
        # return nums1
            
        writeIndex = m + n - 1
        m, n = m-1, n-1
        print(id(nums1))
        while n>=0 and m>=0:
            if nums1[m] > nums2[n]:
                print(id(nums1))
                nums1[writeIndex] = nums1[m]
                print(id(nums1))
                #nums1[m] = float("-inf")           We don't need to change this value because m will be pointing to m-1
                m -= 1
            else:
                nums1[writeIndex] = nums2[n]
                n -= 1
            writeIndex -= 1
        print(id(nums1))
        if n>-1:
            print(id(nums1))
            nums1[0:n+1] = nums2[0:n+1]
            print(id(nums1))
        return nums1

solution=Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(id(solution.merge(nums1, m, nums2, n)))

"""
Вам даны два целочисленных массива nums1 и nums2, отсортированных в неубывающем порядке,
и два целых числа m и n, обозначающих количество элементов в nums1 и nums2 соответственно.

Объедините массивы nums1 и nums2 в один массив, отсортированный в неубывающем порядке.

Конечный отсортированный массив не должен возвращаться функцией, а должен храниться внутри 
массива nums1. Для этого nums1 имеет длину m + n, где первые m элементов обозначают элементы, 
которые должны быть объединены, а последние n элементов имеют значение 0 и должны быть проигнорированы. 
nums2 имеет длину n.
"""