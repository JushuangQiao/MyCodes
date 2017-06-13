class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lens, lent = len(s), len(t)
        if lens != lent:
            return False
        hashs, hasht, off = {}, {}, 0
        while off < lens:
            if not hashs.get(s[off]):
                hashs[s[off]] = t[off]
            if not hasht.get(t[off]):
                hasht[t[off]] = s[off]
            if hashs[s[off]] != t[off] or hasht[t[off]] != s[off]:
                return False
            off += 1
        return True
