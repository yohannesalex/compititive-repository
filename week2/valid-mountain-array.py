class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        elif arr[0] >=arr[1]:
            return False
        else:
            counti=0
            countd=0
            flagi=True
            flagd=True
            i=0
            while i < len(arr)-1:
                if flagi and arr[i] <arr[i+1]:
                    while i <len(arr)-1 and arr[i] <arr[i+1]:
                        counti+=1
                        i+=1
                    flagi=False
                elif flagd and arr[i] > arr[i+1]:
                    while  i <len(arr)-1 and arr[i] > arr[i+1] :
                        countd+=1
                        i+=1
                    flagd=False
                else:
                    return False
            if counti > 0 and countd > 0 and counti + countd == len(arr)-1:
                return True
            return False
           