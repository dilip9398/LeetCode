class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = "a"
        while len(word) < k:
            nw = ""
            for c in word:
                if c == 'z':
                    nw = 'a'
                else:
                    word += chr(ord(c) + 1)
            
            word += nw

        return word[k-1]

        