class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        f = 1
        for i in range(len(nums)):
            ele = nums.pop(i)
            for x in nums:
                f *= x
            answer.append(f)
            nums.insert(i, ele)
            f = 1
        return answer


"""
works , but in O(N^2), O(N) -- not the asnwer tho, they need O(N)
"""
