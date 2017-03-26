class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        tmp = ''.join(S.split('-')).upper()
        leng = len(tmp)
        first = K if leng%K == 0 else leng%K
        ret = tmp[:first]
        while first < leng:
            ret += '-' + tmp[first:first+K]
            first += K
        return ret
