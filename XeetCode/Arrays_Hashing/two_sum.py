class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for outer_index in range(len(nums)):
            for inner_index in range(1, len(nums)):
                if (
                    nums[outer_index] + nums[inner_index] == target
                    and outer_index != inner_index
                ):
                    return [outer_index, inner_index]


"""
first: ineff

O(n^2)

had to brush up on range, but clear now

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            hashmap[num] = index

        for i, n in enumerate(nums):
            tar = target - n
            if tar in hashmap and hashmap[tar] != i:
                return [i, hashmap[tar]]


"""
2 pass

arrived at this sol on my own after learning to use hashmap, was on right path with t = target - n logic
needed to understand the error checking of same index tho

O(n)
o(n)

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            tar = target - n
            if tar in hashmap:
                return [i, hashmap[tar]]
            else:
                hashmap[n] = i


"""
3 pass

most efficent:: learnt online
bascially checking when making the hashmap, seems logical

o(n), o(n)

"""
