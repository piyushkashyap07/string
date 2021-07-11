s=input()
li=[]
j=0
for i in range(len(s)-1,-1,-1):
    li.append(str(s[i]))
s_ans=""
for e in li:
    s_ans=s_ans+e
if(s_ans==s):
    print("true")
else:
    print("false")