class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for each in cpdomains:
            times, domain = each.split()
            n = domain.count('.')
            for i in range(n+1):
                temp = domain.split('.',i)[-1]
                if temp in dic:
                    dic[temp] += int(times)
                else:
                    dic[temp] = int(times)
        
        res = []
        for i in dic:
            res.append(f"{dic[i]} {i}")
        
        return res