from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n == target:
                return i

        return -1

if __name__ == '__main__':
    s = Solution()

    print(s.search([-1, 0, 3, 5, 9, 12], 9))