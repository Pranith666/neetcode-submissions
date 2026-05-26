class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,1
        count=1
        if s=="":
            return 0
        substring=s[l]
        while r<len(s):
            if s[r] in substring:
                l+=1
                r=l+1
                substring=s[l]
            else:
                substring+=s[r]
                # count+=1
                r+=1
            count = max(count, len(substring))
        return count
        