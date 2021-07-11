from sys import stdin


def isPermutation(s, t):
    len1=len(s)
    len2=len(t)
    if len1!=len2:
        return False
    else:
        for j in range(len2):
            if t[j] not in s:
                return False
	#an array is taken for maintaining frequency of characters
        arr=[0]*256
        for char in s:
            order=ord(char)
            arr[order]=arr[order]+1

        for char in t:
            order=ord(char)
            arr[order]=arr[order]-1

        for i in range(256):
            if arr[i]!=0:
                return False
        return True




























#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

