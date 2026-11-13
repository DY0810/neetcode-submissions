class Solution:
    def compress(self, chars: List[str]) -> int:
        p1 = 0
        p2 = 0

        while p2 < len(chars):
            num = 0
            currChar = chars[p2]

            while p2 < len(chars) and chars[p2] == currChar:
                num += 1
                p2 += 1
            
            if num == 1:
                chars[p1] = currChar
                p1 += 1
                continue

            chars[p1] = currChar

            for ch in str(num):
                p1 += 1
                chars[p1] = ch
               
            p1 += 1
       
        return p1