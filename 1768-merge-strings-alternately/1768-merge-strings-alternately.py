class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n1 = len(word1)
        n2 = len(word2)
        s = []
        i = 0
        j =0
        while ( i < n1 and j < n2):
            s.append(word1[i])
            s.append(word2[j])
            i += 1
            j += 1

        while i < n1:
            s.append(word1[i])
            i += 1

        while j < n2:
            s.append(word2[j])
            j += 1
        return "".join(s)


        