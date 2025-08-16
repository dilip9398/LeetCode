class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """

        arr = list(str(num))
        for i in range(len(arr)):
            if arr[i] == "6":
                arr[i] = "9"
                break
        return int("".join(arr))
