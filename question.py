inp=input()
mini=100000
k=len(set(inp))
j=0
i=0
while i<=len(inp):
    if len(set(inp[j:i+1]))==k:
        mini=min(i+1-j,mini)
        j+=1
    else:
        i+=1
print(mini)
