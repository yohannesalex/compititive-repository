class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def _move(nums, idx):
            nextidx = (idx + nums[idx]) % len(nums)
            return nextidx if nextidx >= 0 else len(nums) + nextidx

        if len(nums) < 2:
            return False

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            slow = fast = i
            is_forward = nums[i] > 0
            while True:
                if slow == _move(nums, slow):
                    break
                if _move(nums, fast) == _move(nums, _move(nums, fast)):
                    break
                temp_slow = _move(nums, slow)
                temp_fast = _move(nums, fast)
                temp_fastfast = _move(nums, _move(nums, fast))
                if (nums[temp_slow] > 0) != is_forward:
                    break
                if (nums[temp_fast] > 0) != is_forward:
                    break
                if (nums[temp_fastfast] > 0) != is_forward:
                    break    
                slow = _move(nums, slow)
                fast = _move(nums, _move(nums, fast))
                if slow == fast:
                    return True
        return False