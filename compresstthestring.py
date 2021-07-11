s=input()
li=[]
for i in range(0,len(s)):
    li.append(s[i])
li_ans=[]
n=len(li)
i=0
while i<=n-1:
    temp=li[i]
    count=0
    j=i
    while (li[j]==li[i]):
        count=count+1
        if(j<n-1):
            j=j+1
        else:
            j=j+1
            break
    if(count!=1):
        li_ans.append([temp,count])
    else:
        li_ans.append([temp])
    i=j
for e in li_ans:
    i=0
    while i<=len(e)-1:
        print(e[i],end="")
        i=i+1