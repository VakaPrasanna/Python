s = input("Enter s: ")
k = int(input("Enter k: "))
s1=s.split()
res=""
for i in range(k):
    res+=s1[i]+" "
res=res.strip()
print(res)
---------------------------------------
