class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left, right = 0, len(s) - 1
        l_list, r_list = [], []
        while left < right:
            while left < right and s[left] not in vowels:
                l_list.append(s[left])
                left += 1
            while left < right and s[right] not in vowels:
                r_list.append(s[right])
                right -= 1
            if left < right:
                l_list.append(s[right])
                r_list.append(s[left])
                left += 1
                right -= 1
        if left == right:
            l_list.append(s[left])
        return ''.join(l_list) + ''.join(r_list[::-1])


