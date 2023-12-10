class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        k=defaultdict(lambda :[])
        for i in range(len(paths)):
            s=paths[i]
            lst=s.split(" ")
            for j in range(1,len(lst)):
                sp=lst[j].index("(")
                k[lst[j][sp:]].append(lst[0]+"/"+lst[j][:sp])
        return [k[i] for i in k if len(k[i])>1]
    