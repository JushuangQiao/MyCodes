class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.n = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.n.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.n:
            return self.n.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.n[0]

    def empty(self):
        """
        :rtype: bool
        """
        return self.n == []
