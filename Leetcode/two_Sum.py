from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for h in range(len(nums)):
                if nums[i] + nums[h] == target:
                    if i == h:
                        break
                    else:
                        output = [i,h]
                        return output
                else:
                    continue

if __name__ == "__main__":
    nums1 = Solution()
    indeies = nums1.twoSum([2,7,11,13],9)
    indeies2 = nums1.twoSum([3,2,4],6)
    indeies3 = nums1.twoSum([3,3],6)
    print(indeies)
    print(indeies2)
    print(indeies3)