# https://leetcode.com/problems/remove-element/description/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current_length = len(nums)
        i = 0
        while i < current_length:
            if nums[i] == val:
                nums[i] = nums[current_length - 1]
                current_length -= 1
                continue
            else:
                i += 1
        return current_length
