class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(start, k, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if start < i and nums[i - 1] == nums[i]: # skip non-meaninful movements of a pointer
                        continue

                    quad.append(nums[i]) # add the candidate as a potential quadruplet
                    kSum(i + 1, k - 1, target - nums[i])
                    quad.pop()

                return
            # two sum II problem

            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:

                    res.append(quad+[nums[l], nums[r]])

                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1


        kSum(0, 4, target)
        return res
