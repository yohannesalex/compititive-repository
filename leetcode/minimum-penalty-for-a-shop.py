class Solution:
    def bestClosingTime(self, customers: str) -> int:
        closedin=customers.count("Y")
        mini=closedin
        result = []
        count={closedin:0}
        # for i in range(len(customers)):
        #     if customers[i] == "Y":
        #         closedin-=1

        #     else:
        #         closedin+=1
        #     if closedin < mini:
        #         mini = closedin
        #         result = []

        #     elif closedin == mini:
        #         result.append(i+1)
            
        
        # if not result: return 0
        # else: return result[0]
        for i in range(1,len(customers)+1):
            if customers[i-1] =="Y":
                closedin-=1
                if closedin not in count:
                    count[closedin]=i
            else:
                closedin+=1
                if closedin not in count:
                    count[closedin]=i
        k=min(count)
        return count[k]
            

        