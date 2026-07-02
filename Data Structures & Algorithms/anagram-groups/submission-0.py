class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        grouping = defaultdict(list)
        for s in strs:
             key = ''.join(sorted(s))
             grouping[key].append(s)
        return list(grouping.values())