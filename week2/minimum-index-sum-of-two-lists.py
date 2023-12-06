class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count=[]
        strings=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    strings.append(list1[i]) 
                    count.append(i+j)
        
        if len(count)<=1:
            return strings
        else:
            
            res=[]
            mini=min(count)
            for i in range(len(count)):
                if count[i] == mini:
                    res.append(strings[i])
                elif res and count[i] != mini:
                    break
            return res