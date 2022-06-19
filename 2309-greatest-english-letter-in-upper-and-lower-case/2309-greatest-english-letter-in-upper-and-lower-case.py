class Solution(object):
    def greatestLetter(self, s):
        counter1=""
        counter2=""
        c3=''
        c4=''
        for i in s:
            if i.isupper():
                counter1+=i
        for j in s:
            if j.islower():
                counter2+=j
        c3=counter2.upper()
        for x in counter1:
            for y in c3:
                if x==y:
                    c4+=x
        if c4=="":
            return c4
        else:
            return max(c4)
        