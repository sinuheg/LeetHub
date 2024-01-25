class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        last_flower = -2
        planted = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i - last_flower >= 2:
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        planted += 1
                        last_flower = i
                        i += 1
                i += 1
            else:
                last_flower = i
                i += 1
        return planted >= n
