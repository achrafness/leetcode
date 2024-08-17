# beats 98.24% of python submissions.   
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        seen = set()
        for item in strs:
            sorted_string =  "".join(sorted(item))
            if sorted_string in seen:
                hash[sorted_string].append(item)
            else:
                seen.add(sorted_string)
                hash[sorted_string] = [item]        
        return list(hash.values())

