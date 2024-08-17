# beat 95.09% of python submissions.
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}
        for item in nums:
            if item in hash:
                hash[item] += 1
            else:
                hash[item] = 1
        hash = sorted(hash.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in hash[:k]]