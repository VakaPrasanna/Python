38. Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
--------------------------------------------------------------------------------------------------------------------

def count_and_say(n: int)->str:
    if n==1:
        return "1"
    prev=count_and_say(n-1)
    res=""
    cnt=1
    
    for i in range(1,len(prev)+1):
        if i<len(prev) and prev[i]==prev[i-1]:
            cnt=cnt+1
        else:
            res=res+str(cnt)+prev[i-1]
            cnt=1
    return res
    
n=int(input())
print("Output: ",count_and_say(n))
------------------------------------------------------------------------------------------------------------------
