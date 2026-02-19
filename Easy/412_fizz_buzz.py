import typing

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            r, three, five = "", i % 3 == 0, i % 5 == 0
            
            if three:
                r += 'Fizz'
            if five:
                r += 'Buzz'
            if not three and not five:
                r = str(i)
            ans.append(r)
        
        return ans