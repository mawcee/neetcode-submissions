class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_list = set()
        for x in nums:
            if x not in temp_list:
                temp_list.add(x)
            else:
                return True
        return False

        [1,2,3,4,5]
        