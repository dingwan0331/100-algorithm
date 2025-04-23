class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1_size, num2_size = len(nums1), len(nums2)
        total_len = num1_size + num2_size
        idx = 0
        is_odd = total_len % 2 != 0
        target_idx = total_len // 2 if is_odd else total_len // 2 - 1
        for i in range(total_len):
            nums1, nums2, item = self.get_max_item(nums1, nums2)
            if idx == target_idx:
                if is_odd:
                    return float(item)
                else:
                    _, _, item1 = self.get_max_item(nums1, nums2)
                    return (item + item1) / 2
            idx += 1

    def get_max_item(self, list1: List[int], list2: List[int]):
        if len(list1) == 0:
            result = list2.pop()
            return list1, list2, result
        elif len(list2) == 0:
            result = list1.pop()
            return list1, list2, result
        else:
            item1, item2 = list1.pop(), list2.pop()
            if item1 > item2:
                list2.append(item2)
                return list1, list2, item1
            else:
                list1.append(item1)
                return list1, list2, item2
