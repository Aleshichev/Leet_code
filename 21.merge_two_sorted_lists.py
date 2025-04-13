# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def from_list(values):
    dummy = ListNode()  # фиктивная голова
    current = dummy
    for val in values:
        current.next = ListNode(val)  # создаём новый узел
        current = current.next  # двигаемся вперёд
    return dummy.next


list1 = from_list([1, 2, 4])
list2 = from_list([1, 3, 4])
# Input: list1 = [1,2,4], list2 = [1,3,4] Output: [1,1,2,3,4,4]
# Input: list1 = [], list2 = [] Output: []
# Input: list1 = [], list2 = [0] Output: [0]


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next


Solution().mergeTwoLists(list1, list2)
