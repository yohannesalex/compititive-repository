class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill = {}
        for i in bills:
            print(bill,i)
            if i== 10:
                if 5 not in bill:
                    return False
                else:
                    bill[5]-=1
                    if bill[5]==0:
                        del bill[5]
            if i == 20:
                if 10 in bill:
                    bill[10]-=1
                    if bill[10]==0:
                        del bill[10]
                    if not 5 in bill:
                        return False
                    else:
                        bill[5]-=1
                        if bill[5]==0:
                            del bill[5]
                else:
                    if 5 not in bill:
                        return False
                    elif bill[5]<3:
                        return False
                    else:
                        bill[5]-=3
                        if bill[5]==0:
                            del bill[5]
                


            bill[i] = 1 + bill.get(i,0)
        return True


