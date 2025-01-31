import re
class Solution(object):
    def isPalindrome(self, s):
        st=[]
        s=list(s)
        for i in range(len(s)):
            if s[i].isalnum():
                s[i]=s[i].lower()
                st.append(s[i])
        st="".join(st)
        print(st)
        print(st[::-1])
        if st[::-1]==st:
            return True
        else:
            return False


            
            

            

       
