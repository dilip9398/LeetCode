class Solution(object):
    def addBinary(self, a, b):
        a1=int(a, 2)
        b1=int(b, 2)
        while(b1!=0):
            carry = a1 & b1
            a1 = a1^b1
            b1 = carry<<1
        return bin(a1)[2:]
        