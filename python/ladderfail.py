k=int(input())
lst=[]
for _ in range(k+1):
    lst.append([])
len1=[1]*(k+1)

lst[0]=[-1]  # lst[0]
for i in range(1,k):  
    nums = list(map(int,input().split()))
    lst[i]=nums  # lst[1]~lst[k-1]
    len1[i]=len(nums)
lst[k]=[-1]  #lst[k]
print(lst)
# 1(a) 는 lst[1] 만, 2(b) 는 lst[1],lst[2] , 3(c) 는 lst[2],lst[3] 만.. k는 lst[k-1]
# lst 바깥부분 1-based, lst 안쪽부분 0-based

step=[0]*(k+1) # index 기준
anslst=[0] * (k+1)

for i in range(1,k+1):
    depth=-2

    kvalue=i
    while 1:
        idx1=step[kvalue-1]
        idx2=step[kvalue]
        # min(min(lst[i-1]),min(lst[i]))
        # =depth 일때도 멈춰야함
        if lst[kvalue-1][idx1]<lst[kvalue][idx2]:
            depth = lst[kvalue-1][idx1]
            kvalue-=1
        else:
            depth = lst[kvalue][idx2]
            kvalue+=1

        for a in range(1,k):
            idx3 = step[a]
            while lst[a][idx3]<depth:
                step[a]+=1
        

        
alps="Sabcdefghijklmnopqrstuvwxyz" # 1-based 로 고치기 위해 가장 앞에 아무문자 붙이기!
for a in range(1,k+1):
    print(alps[anslst[a]],end=' ')
