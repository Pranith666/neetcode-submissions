class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict=defaultdict(list)
        for i,n in enumerate(numbers):
            diff=target-n
            if diff in num_dict:
                return [ num_dict[diff]+1,i+1]
            num_dict [n] = i