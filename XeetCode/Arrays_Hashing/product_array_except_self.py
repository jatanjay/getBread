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

what I learnt: 


1. CAN JUST DO: for i in reversed([1,2,3])!


"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        left, right = 1, 1

        for i in range(len(nums)):
            answer[i] = left
            left *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer


"""
idea 


from left, ans[i] = everything on the left
for i = 0, 1
and then, 1 =* num[i]

same for right
only thing now is, we need multiply it with the left stored stuff as well



left = [x x x x]
        | | | |
        * * * *    
right = [x x x x]
this is optimal, since we are are not storing and creating 2 arrays called left, right

hence in O(N)


"""
