class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        d_nums = nums*2
        nums[:] = d_nums[len(nums)-k:2*len(nums)-k]
        