class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict = {}
        for i in ransomNote:
            dict[i] = dict[i] + 1 if i in dict else  1
        for c in dict:
            if magazine.count(c) < dict[c]:
                return False
        return True
