# beat 65.28% of python submissions in 35ms run time.
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(t) != len(s)):
            return False
        first_hash , second_hash = {} , {}
        for i in range(len(t)):
            first_hash[t[i]] = first_hash.get(t[i],0) + 1
            second_hash[s[i]]= second_hash.get(s[i],0) + 1
        return  second_hash == first_hash

