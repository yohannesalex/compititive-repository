class ATM:

    def __init__(self):
        self.atm=[0,0,0,0,0]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(0,5):
            self.atm[i]+=banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:

        result=[0,0,0,0,0] 

        if amount>=500 and self.atm[4]>=1:
            total=amount//500 
            m=min(total,self.atm[4]) 
            amount=amount-(500*m) 
            if self.atm[4]-m<=0:
                self.atm[4]=0 
            else:
                self.atm[4]-=m

            result[4]+=m 
        
        if amount>=200 and self.atm[3]>=1:
            total=amount//200 
            m=min(total,self.atm[3]) 
            amount=amount-(200*m) 
            if self.atm[3]-m<=0:
                self.atm[3]=0 
            else:
                self.atm[3]-=m
                
            result[3]+=m

        if amount>=100 and self.atm[2]>=1:
            total=amount//100 
            m=min(total,self.atm[2]) 
            amount=amount-(100*m) 
            if self.atm[2]-m<=0:
                self.atm[2]=0 
            else:
                self.atm[2]-=m
                
            result[2]+=m 

        if amount>=50 and self.atm[1]>=1:
            total=amount//50 
            m=min(total,self.atm[1]) 
            amount=amount-(50*m) 
            if self.atm[1]-m<=0:
                self.atm[1]=0 
            else:
                self.atm[1]-=m
                
            result[1]+=m

        if amount>=20 and self.atm[0]>=1:
            total=amount//20 
            m=min(total,self.atm[0]) 
            amount=amount-(20*m) 
            if self.atm[0]-m<=0:
                self.atm[0]=0 
            else:
                self.atm[0]-=m
                
            result[0]+=m


        if amount!=0:
            for i in range(0,5):
                self.atm[i]+=result[i] 
            return [-1]
        else:
            return result




# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)