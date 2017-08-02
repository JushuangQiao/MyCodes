class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not s or not g:
            return 0
        g.sort()
        s.sort()
        counts = 0
        son, cook = 0, 0
        while son < len(g) and cook < len(s):
            if s[cook] >= g[son]:
                counts += 1
                son += 1
            cook += 1
        return counts
