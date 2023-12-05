class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res=1
        k=capacity
        capacity-=plants[0]
        for i in range(1,len(plants)):
            
            if capacity >= plants[i]:
                capacity-=plants[i]
                res+=1
            else:
                res+=2*(i)+1
                capacity=k
                capacity-=plants[i]
        return res
                
