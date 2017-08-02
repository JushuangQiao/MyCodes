class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        c = Counter(s)
        # sor = sorted(c.items(),key=lambda x:x[1],reverse=True)
        return ''.join([i[0]*i[1] for i in c.most_common()])

