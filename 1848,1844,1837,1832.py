nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 0
min_diff=float('inf')
for i in range(start,len(nums)):
    if nums[i]==target:
        if abs(i-start)<min_diff:
            min_diff=abs(i-start)
print(min_diff)

#return min(abs(i - start) for i, x in enumerate(nums) if x == target)

-----------------

s = "a1b2c3d4e"
#Output: "abbdcfdhe"
res=""
for i,x in enumerate(s):
    if x.isdigit():
        r=chr(ord(s[i-1])+int(x))
        res+=r
    else:
        res+=x
        
print(res)
-------------------------
n = 34
k = 6
sum=0
while n:
    rem=n%k 
    sum+=rem
    n//=k 
print(sum)

---------------------------------

def isPangram(sentence):
    if len(set(sentence)) == 26:
        return True
    else:
        return False
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(isPangram(sentence))
