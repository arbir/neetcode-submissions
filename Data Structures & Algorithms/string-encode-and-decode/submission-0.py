class Solution:

    def encode(self, strs: List[str]) -> str:
        size=len(strs)
        st2=""
        for s in strs:
            l=len(s)
            #format [length]+#+[string]
            st2+=f"{l}#{s}"
        return st2
            


    def decode(self, s: str) -> List[str]:
        st1=[]
        size=len(s)
        i=0
        
        while i<size:
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            st1.append(s[j+1:j+1+length])
            i=j+1+length
        return st1


