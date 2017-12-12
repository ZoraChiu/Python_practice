"""
https://leetcode.com/problems/intersection-of-two-arrays/description/

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

"""
nums1 = [1, 2, 2, 1, 4, 5]
nums2 = [2, 2, 1, 5]

def intersection(list1, list2):
    intersection_list = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                intersection_list.append(list1[i])
    print(set(intersection_list))

intersection(nums1, nums2)
