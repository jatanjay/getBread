# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits = digits[::-1]
#         carry = True
#         curr_index = 0

#         while carry:
#             if curr_index < len(digits):
#                 if digits[curr_index] == 9:
#                     digits[curr_index] = 0
#                 else:
#                     digits[curr_index] += 1
#                     carry = False
#             else:
#                 digits = digits + [1]
#                 carry = False
#             curr_index += 1
#         return digits[::-1]


# """
# First solution was converting everything to int, adding and then converting back to string(list) / quick and dirty but probally not what the interviewer wants
# """

# """
# this solution, i looked online


# loooping from back, since we want to start from LSB


# while flag:


# """


def isHappy(n):

    # if len(str(n)) == 1 and n != 1:
    #     return False

    if n == 1:
        return True

    res = n
    result = False
    trys = 0
    while not result and trys < 100:
        nums = list(str(res))
        sq_add = sum([int(x) ** 2 for x in nums])
        if sq_add != 1:
            res = sq_add
            trys += 1
        else:
            result == True
            return True
    else:
        return False

f = isHappy(8)
print(f)
