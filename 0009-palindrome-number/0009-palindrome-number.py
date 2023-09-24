class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stringX=str(x)
        if stringX[::-1]==str(x):
            return True 
        return False

        