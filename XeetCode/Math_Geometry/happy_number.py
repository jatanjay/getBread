class Solution:
    def isHappy(self, n):

        if n == 1:
            return True

        res = n
        result = False
        trys = 0
        while not result and trys < 10:
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


"I did it this way, by breaking recursion count"
