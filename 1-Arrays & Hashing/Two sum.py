# Beat 99.31% of python submissions in 26ms run time.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map ={}
        for index,item in enumerate(nums):
            difference = target - item
            if difference in hash_map:
                return [hash_map[difference],index]
            hash_map[item] = index

