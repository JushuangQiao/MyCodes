class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        ds = {}
        dg = {}
        a, b = 0, 0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                a += 1
            else:
                ds[secret[i]] = ds.get(secret[i], 0) + 1
                dg[guess[i]] = dg.get(guess[i], 0) +1
        for i in dg:
            if i in ds:
                b += min(ds[i], dg[i])
        return '{0}A{1}B'.format(a, b)
