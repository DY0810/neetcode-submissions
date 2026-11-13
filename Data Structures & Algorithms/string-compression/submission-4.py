class Solution:
    def compress(self, chars: List[str]) -> int:
        p1 = 0
        p2 = 0
        s = ""

        while p2 < len(chars):#11
            num = 0
            currChar = chars[p2]
            print(currChar)

            while p2 < len(chars) and chars[p2] == currChar:
                num += 1
                p2 += 1
            #5 5
            print(p2)
            if num == 1:
                s += currChar
                chars[p1] = currChar
                p1 += 1
                continue

            s += currChar + str(num)
            chars[p1] = currChar

            for ch in str(num):
                p1 += 1
                chars[p1] = ch
               
            p1 += 1
        
        return len(s)