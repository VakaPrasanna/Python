Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
-------------------------------------
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
-------------------------------------

def fun(n):
    is_neg=False
    if n<0:
        is_neg=True
    res=0
    num=abs(n)
    while num>0:
        last_digit=num%10
        res=(res*10)+last_digit
        num//=10
    if res< (-(2**31)) or res> ((2**31)-1):
        return 0
    return -res if is_neg else res
n=int(input("Enter number: "))
print(fun(n))
