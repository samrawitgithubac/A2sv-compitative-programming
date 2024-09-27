class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashtable={}
        for i in s:
            if i in hashtable:
                hashtable[i]+=1
            else:
                hashtable[i]=1

                 
        for i in t:
            if i not in hashtable or hashtable[i]==0:

                return i
            else:
                hashtable[i]-=1

           
        