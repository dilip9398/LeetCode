class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        # word = "a"
        
        # while len(word) < k:
           
        #     for operation in operations:
        #         nw =""
        #         if operation == 0:
        #             for c in word:
        #                 nw += c
        #         else:
        #             for c in word:
        #                 transformed = chr(ord(c) + 1)
        #                 nw += transformed

        #         word = nw + word
        #         if len(word) >= k:
        #             break
                   
        
            
        # return word[k-1]

        k -= 1
        current = 0
        for index, op in enumerate(operations):
            if ((1 << index) & k) > 0:
                if op == 1:
                    current = (current + 1) % 26

        return chr(ord('a') + current)
        