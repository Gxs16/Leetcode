class Solution:
    def fill_stack(self, nums, target_length):
        stack = []
        length = len(nums)
        for i, num in enumerate(nums):
            while stack and target_length-len(stack) < length-i and num > stack[-1]:
                stack.pop()
            if len(stack) < target_length:
                stack.append(num)
        return stack

    def merge(self, nums1, nums2):
        result = []
        while nums1 or nums2:
            if not nums1:
                result.extend(nums2)
                break
            elif not nums2:
                result.extend(nums1)
                break
            else:
                if nums1[0] > nums2[0]:
                    result.append(nums1.pop(0))
                elif nums1[0] < nums2[0]:
                    result.append(nums2.pop(0))
                else:
                    l1, l2 = 1, 1
                    while l1 < len(nums1) and l2 < len(nums2):
                        if nums1[l1] == nums2[l2]:
                            l1 += 1
                            l2 += 1
                        elif nums1[l1] > nums2[l2]:
                            result.append(nums1.pop(0))
                            break
                        else:
                            result.append(nums2.pop(0))
                            break
                    else:
                        if len(nums1) >= len(nums2):
                            result.append(nums1.pop(0))
                        else:
                            result.append(nums2.pop(0))
        return result

    def maxNumber(self, nums1, nums2, k):
        result = []
        if len(nums1) > len(nums2):
            num_short, num_long = nums2, nums1
        else:
            num_short, num_long = nums1, nums2
        for i in range(min(len(num_short)+1, k+1)):
            if k-i > len(num_long):
                continue
            stack1 = self.fill_stack(num_short, i)
            stack2 = self.fill_stack(num_long, k-i)
            merge_result = self.merge(stack1, stack2)
            if not result:
                result = merge_result
            else:
                for i in range(k):
                    if result[i] == merge_result[i]:
                        continue
                    elif result[i] > merge_result[i]:
                        break
                    else:
                        result = merge_result
                        break
        return result