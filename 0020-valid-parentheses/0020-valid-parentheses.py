class Solution(object):
    def isValid(self, s):
        st=[]
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                st.append(ch)
            else:
                if len(st)==0:
                    return False
                
                if ((st[-1]=='(' and ch==')')or 
                    (st[-1]=='{' and ch=='}')or
                    (st[-1]=='[' and ch==']')):
                    st.pop()
                else:
                    return False
        return len(st)==0
        