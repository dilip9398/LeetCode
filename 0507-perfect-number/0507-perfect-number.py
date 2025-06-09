import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2 : return False
        divisiorcount = 1
        square = math.isqrt(num)
        for i in range(2, square + 1 ):
            if num % i == 0:
                divisiorcount += i
                if num // i != i :
                    divisiorcount += num // i
                
        return divisiorcount == num