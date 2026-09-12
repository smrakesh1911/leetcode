class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            y = target - num
            if y in seen:
                return [seen[y], i]
            seen[num] = i


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i, num in enumerate(nums):
#             y = target - num
#             if y in nums[i + 1:]:
#                 y_index = nums.index(y, i + 1)
#                 return [i, y_index]


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             y = target - nums[i]
#             if y in nums[i + 1:]:
#                 y_index = nums.index(y, i + 1)
#                 return [i, y_index]