# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap={}
        res=[]
        for cp in cpdomains:
            parts=cp.split(" ")
            
            count=parts[0]
            domain=parts[1]
            dom=domain.split(".")
            for i in range(len(dom)):
                m=".".join(dom[i:])
                if m not in hashmap:
                    hashmap[m] = count
                else:
                    hashmap[m] = str(int(count)+int(hashmap[m]))
        for j in hashmap:
            res.append(hashmap[j]+" "+j)
        return res
            
            