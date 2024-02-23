class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
       
        if rowIndex == 0:
            return [1]
        pre = self.getRow(rowIndex-1)
        cur=[1]
        for i in range(1,len(pre)):
            cur.append(pre[i]+pre[i-1])
        cur.append(1)
        return cur