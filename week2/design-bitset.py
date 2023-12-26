class Bitset:

    def __init__(self, size: int):
        self.a=[0]*size
        self.on=0
        self.n = size
        self.flipped=False

    
    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.a[idx]==1:
                self.on+=1
                self.a[idx]=0
        else:
            if self.a[idx]==0:
                self.on+=1
                self.a[idx]=1

    
    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.a[idx]==0:
                self.on-=1
                self.a[idx]=1
        else:
            if self.a[idx]==1:
                self.on-=1
                self.a[idx]=0

    
    def flip(self) -> None:
        if self.flipped:
            self.flipped=False
        else:
            self.flipped=True
        self.on = self.n-self.on
    
    
    def all(self) -> bool:
        if self.n==self.on:
            return True
        return False

    
    def one(self) -> bool:
        if self.on>0:
            return True
        return False

    
    def count(self) -> int:
        return self.on
        
        
    def toString(self) -> str:
        s=""
        if self.flipped:
            for i in self.a:
                if i:
                    s+="0"
                else:
                    s+="1"
            return s
        for i in self.a:
            if i:
                s+="1"
            else:
                s+="0"
        return s