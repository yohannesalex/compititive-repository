# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1 and flowerbed == [0] and n == 1:
            return True
        if len(flowerbed) >= 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            n-=1
            flowerbed[0] = 1
        if len(flowerbed) >= 2 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n-=1
            flowerbed[-1] = 1

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n-=1
                flowerbed[i] = 1
        return n <= 0