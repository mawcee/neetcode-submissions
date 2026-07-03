class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = defaultdict(int)
        for x in nums:
            frequency_dict[x] += 1
        frequency_list = sorted(frequency_dict.items(), key= lambda x: x[1], reverse = True)
        return [pair[0] for pair in frequency_list[:k]]