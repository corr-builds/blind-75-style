class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], [] # final result, a quadruplet

        def KSum(k, start, target):

            if k != 2:
                for i in range(start, len(nums) - k + 1): # start at a pointer, i
                    if start < i and nums[i - 1] == nums[i]: # skip non-meaninful movements of a pointer
                        continue

                    quad.append(nums[i]) # add the current pointer to the current quadruplet
                    KSum(k - 1, i + 1, target - nums[i]) # make a recursive call. this call will execute the above code (up to the KSum method signature), adding a new pointer in an iterative fashion, up until (and including) when it hits the base case. After the base case, the method will return. Then, the other recursive calls will start to return cleaning up the element the added to quad (quad.pop()) before they do so. Considering that each iteration has a recursive call (forming a line of calls rather than a recursive tree of calls), we can state in a more non-technical way that for each i (the first of k pointers) we recurse, adding another ith pointer, until the number of pointers is 2. This helps solve the Xsum (Ksum) problem, which essentially, for any number of pointers, boils down to the Ksum problem except for the base case when there are 2 pointers, at which piont we can solve like 2sum II - input array is sorted problem
                    quad.pop()

                return

            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

        KSum(4, 0, target)
        return res
