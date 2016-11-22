class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        shash = {}
        max_sub_len = 0
        left = 0
        right = 0
        
        for k,v in enumerate(s):
            if v in shash:
                left = left if left > shash[v] + 1 else shash[v] + 1
            shash[v] = k
            max_sub_len = max_sub_len if max_sub_len > right - left + 1 else right - left + 1
            right += 1
        return max_sub_len
