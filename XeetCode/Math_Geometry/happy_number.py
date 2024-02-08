# # class Solution:
# #     def isHappy(self, n):

# #         if n == 1:
# #             return True

# #         res = n
# #         result = False
# #         trys = 0
# #         while not result and trys < 10:
# #             nums = list(str(res))
# #             sq_add = sum([int(x) ** 2 for x in nums])
# #             if sq_add != 1:
# #                 res = sq_add
# #                 trys += 1
# #             else:
# #                 result == True
# #                 return True
# #         else:
# #             return False


# # "I did it this way, by breaking recursion count"


# class Solution:
#     def isHappy(self, n):
#         seen = set()
#         while n not in seen:
#             seen.add(n)
#             n = sum(int(i) ** 2 for i in str(n))
#             if n == 1:
#                 return True
#         return False


# """
# this is using hashmap

# the idea is keeping tabs whether the 'n' is seen or not before (is it entering a cycle?)
# """

# O(k*d) (# k cycles, d digits),
# Space: O(n) (# saved in set)
