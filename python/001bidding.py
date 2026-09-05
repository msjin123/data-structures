n=int(input())
lst=[]
for i in range(n):
    name,p=input().split()
    lst.append([name,int(p)])


lst.sort(key=lambda a: a[1],reverse=True)

z=False
ans="NONE"
for i in range(n):
    if i==0 or lst[i-1][1]>lst[i][1]:
        z=False
    else:
        z=True
    if z:
        continue

    # z==false 일떄만 진행
    if i==n-1 or lst[i][1]>lst[i+1][1]:
        ans=lst[i][0]
        break

    
print(ans)

        
