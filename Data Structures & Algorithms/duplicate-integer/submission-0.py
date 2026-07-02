class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_list = []
        for x in nums:
            if x not in temp_list:
                temp_list.append(x)
            else:
                return True
        return False
        