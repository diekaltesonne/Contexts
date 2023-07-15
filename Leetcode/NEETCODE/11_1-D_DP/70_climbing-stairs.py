from typing import List
# - [How to Convert a Python String to int](https://realpython.com/convert-python-string-to-int/)

class Solution:
    def climbStairs(self, m: int) -> int:
        prev = 0 
        prev2 = 1
        c = [] 
        for i in range(0,m):
            c.append([prev,prev2]) 
            cur = prev + prev2
            prev = prev2
            prev2 = cur
            
        print(c)
        return cur 

def main():
    a = Solution()
    print(a.climbStairs(m= 2))
    print(a.climbStairs(m = 3))
    print(a.climbStairs(m = 4))



if __name__ == "__main__":
    main()