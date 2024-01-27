class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            a = nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                b = nums[j]
                c = nums[k]
                if a + b + c == 0:
                    result.append((a, b, c))
                    #k-=1 <- alternative. which one to move at this point is arbitrary
                    j+=1
                elif a + b + c > 0:
                    k-=1
                else:
                    j+=1

        return set(result)     
