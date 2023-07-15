class Solution:
    def reverse(self, x: int) -> int:   
        ans = str(x)[::-1]
        a = 0
        
        if ans.endswith('-'):
            print(ans)
            l = len(ans)
            ans = ans[:l-1]
            a = 1
        
        if(abs(int(ans))<= 0x7FFFFFFF):
            if(a == 1):
                return int(ans) * (-1) 
            else:
                return int(ans) 
        else:
            return 0