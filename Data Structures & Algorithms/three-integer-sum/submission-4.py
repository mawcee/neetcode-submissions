class Solution:
    def threeSum(self, nums):
        nums.sort()                              # sort so two pointers + dup-skip work
        res = []

        for i in range(len(nums)):
            a = nums[i]                          # the "locked in" number this round

            if a > 0:                            # sorted: if a is positive, no triplet
                break                            #   can sum to 0 → stop entirely

            if i > 0 and nums[i] == nums[i-1]:   # same a as last round → skip
                continue                         #   (avoids duplicate a triplets)

            l, r = i + 1, len(nums) - 1          # Two Sum II on everything after a
            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:                    # too big → shrink → pull right down
                    r -= 1
                elif total < 0:                  # too small → grow → push left up
                    l += 1
                else:                            # found a triplet!
                    res.append([a, nums[l], nums[r]])
                    l += 1                        # both used → move both inward
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:  # skip duplicate lefts
                        l += 1
        return res