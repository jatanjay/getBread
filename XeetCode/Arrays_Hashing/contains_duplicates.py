"""
Given an integer array nums, return true
if any value appears at least twice in the array, and return false if every element is distinct.
"""


# my solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True


# other solution (use "HASHMAP")
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


# same idea, second is considered more "PYTHONIC"
"""
first try:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for curr in nums:
            count = nums.count(curr)

            if count >= 2:
                return True
            elif count == 1:
                return False


Whats wrong:
Here, I didn't pay attention to the control flow of the return logic.
Consider test case: [2,14,18,22,22]
if count of 2 is 1 (which it is, it directly goes to False, and exits

moral: pay attention to control flow and see how returning will exit the code

Time Complexity: O(n) since, set(nums) creates set after checking each n element
Space: O(n) since it stores the set in memory, length of nums

"""
