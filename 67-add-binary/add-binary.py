class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1=len(a)
        sum1=0
        l2=len(b)
        sum2=0
        str1=""
        if a == "0" and b =="0":
            return "0"
        for i1 in a:
            sum1=sum1+2**l1*int(i1)
            l1=l1-1
        for i2 in b:
            sum2=sum2+2**l2*int(i2)
            l2=l2-1
        t_sum=sum1+sum2
        while t_sum > 0:
            if t_sum % 2 == 0:
                str1="0"+str1
            else:
                str1="1"+str1
            t_sum=t_sum//2

        return str1[:-1:]



        