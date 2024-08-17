# beats 79.45% of python submissions.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = set()
        for item in nums:
            if item in hash :
                return True
            hash.add(item)
        return False