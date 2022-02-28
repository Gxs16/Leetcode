class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pre_sum = 0
        pre_sum_dict = {0:-1}
        post_sum = 0
        post_sum_dict = {0:-1}
        min_pre = 10**6
        min_post = 10**6
        result = [0]*(len(arr))
        result[-1] += 10**6
        for i in range(len(arr)):
            pre_sum+=arr[i]
            pre_sum_dict[pre_sum] = i
            post_sum+=arr[-i-1]
            post_sum_dict[post_sum] = i
            if pre_sum-target in pre_sum_dict:
                min_pre = min(min_pre, i-pre_sum_dict[pre_sum-target])
            result[i] += min_pre
            if post_sum-target in post_sum_dict:
                min_post = min(min_post, i-post_sum_dict[post_sum-target])
            result[len(arr)-i-2] += min_post
        res = min(result)
        if res > 10**5:
            return -1
        else:
            return res