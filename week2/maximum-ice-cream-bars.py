class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        max_value = max(costs)
        count = [0] * (max_value + 1)
        for num in costs:
            count[num] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        output = [0] * len(costs)
        for num in reversed(costs):
            output[count[num] - 1] = num
            count[num] -= 1
        res=0
        print(output)
        for i in output:
            coins-=i
            res+=1
            if coins < 0:
                return res-1
            
        return res

