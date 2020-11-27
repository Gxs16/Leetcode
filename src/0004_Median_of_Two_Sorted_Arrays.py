'''
@Author: Xinsheng Guo
@Time: 2020-11-02 22:47
@File: 0004_Median_of_Two_Sorted_Arrays.py
@Link: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
'''

class SolutionV1:
    '''
    直观思路
    '''
    def appendelement(self, nums1, nums2, merged):
        '''
        合并两个数组，找出中位数
        '''
        if nums1 and nums2:
            length = len(merged)
            if len(nums1+nums2) == length:
                return merged[-1]/2 + min((nums1[0], nums2[0]))/2
            if nums1[0] > nums2[0]:
                merged.append(nums2[0])
                nums2 = nums2[1:]
            elif nums1[0] < nums2[0]:
                merged.append(nums1[0])
                nums1 = nums1[1:]
            else:
                merged.extend([nums1[0], nums2[0]])
                nums1 = nums1[1:]
                nums2 = nums2[1:]
            if len(nums1+nums2) == length:
                return merged[-1]
            return self.appendelement(nums1, nums2, merged)
        else:
            merged.extend(nums1+nums2)
            return (merged[len(merged)//2]+merged[(len(merged)-1)//2])/2


    def findMedianSortedArrays(self, nums1, nums2) -> float:
        '''
        入口
        '''
        merged = []
        return self.appendelement(nums1, nums2, merged)

class SolutionV2:
    '''
    二分查找
    2020-11-4 23:39:54
    '''
    def find(self, nums1, nums2, k):
        while k > 0:
            if nums1 and nums2:
                alpha = min((k-1)//2, len(nums1)-1)
                beta = min((k-1)//2, len(nums2)-1)
                if nums1[alpha] <= nums2[beta]:
                    nums1 = nums1[alpha+1:]
                    k -= (alpha+1)
                else:
                    nums2 = nums2[beta+1:]
                    k -= (beta+1)
            else:
                merged = nums1+nums2
                return merged[k]
        if nums1 and nums2:
            return min(nums1[0], nums2[0])
        else:
            merged = nums1+nums2
            return merged[0]

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        '''
        入口
        '''
        k = len(nums1+nums2)
        if k%2:
            result = self.find(nums1, nums2, k//2)
        else:
            result = self.find(nums1, nums2, k//2)/2 + self.find(nums1, nums2, k//2-1)/2
        return result
        

nums1 = [0,0,0,0,0]
nums2 = [-1,0,0,0,0,0,1]
a = SolutionV2()
print(a.findMedianSortedArrays(nums1, nums2))