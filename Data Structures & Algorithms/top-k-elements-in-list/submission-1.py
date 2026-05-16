class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        res2=[]
        res = defaultdict(int)
        for i in nums:
            res[i]+=1
        for i in range(k):
            max_key = max(res,key=res.get)
            res.pop(max_key)
            res2.append(max_key)
        return res2
        