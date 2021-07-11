def a(rev):
    i=len(rev)-1
    li_ans=[]
    s1=""
    while i>=0:
        li_ans.append(rev[i])
        i=i-1
    for e in li_ans:
        s1=s1+e
    return s1
    
s=input()
li=s.split()
str_ans=""
for i in range(0,len(li)):
    temp=li[i]
    str_ans=str_ans+a(temp)+" "
print(str_ans)