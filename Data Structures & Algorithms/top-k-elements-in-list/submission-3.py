class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        dic = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            dic[num] = 1 + dic.get(num,0)
        for i,j in dic.items():
            freq[j].append(i)
        res=[]
        for i in range(len(nums),0,-1):
            for num in freq[i]:
                res.append(num)
            if len(res)==k:
                return res
