class Solution:
    def minSubarray(self, nums: List[int], target_sum: int) -> int:
        total_sum = sum(nums) % target_sum
        if total_sum == 0:
            return 0

        current_sum, result = 0, len(nums)
        remainder_dict = {0: -1}

        for i, num in enumerate(nums):
            current_sum += num
            remain = current_sum % target_sum
            temp = (remain - total_sum) % target_sum

            if temp in remainder_dict:
                result = min(result, i - remainder_dict[temp])

            remainder_dict[remain] = i

        return result if result < len(nums) else -1
