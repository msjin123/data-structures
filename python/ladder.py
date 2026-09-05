k=int(input())
# lst=[]
# for _ in range(k-1):
#     lst.append([])
lst=[[] for _ in range(k-1)]

for i in range(k-1):
    nums = list(map(int,input().split())) # 마지막 -1은 추가 x
    lst[i]=nums
    # for j in range(len(nums)):
    #     lst[i].append(nums[j]) # i번 -> i+1번 or i+1번 -> i번으로 이동 가능한 행
# print(lst)
# 0(a) 는 lst[0] 만, 1(b) 는 lst[0],lst[1] , 2(c) 는 lst[1],lst[2] 만..
answer_lst=[0]*k        


for i in range(0,k):
    idx1 = i
    present = -1       # 이걸 매 i마다 초기화시켜줬어야 했는데 안시켜줘서 시간 많이 씀.
    while 1:
        end1=False
        end2=False
        min0=-1
        min1=1001
        min2=1001
        
        # idx1 = i-1  (i==0 일떄 빼고 다 실행)
        
        if idx1==0:
            end1=True
        else:
            for num1 in lst[idx1-1]:
                if num1==-1:
                    end1=True
                    break
                if num1>present:
                    min1=num1
                    break
            
        # idx1 = i   (i==k-1일때 빼고 다 실행)
        if idx1==k-1:  
            end2=True
        else:    
            for num1 in lst[idx1]:
                if num1==-1:
                    end2=True
                    break
                if num1>present:
                    min2=num1
                    break
        
        # i번째열 사다리에서 출발해서 idx1번째열 사다리로 도착
        # print(end1,end2)
        if end1 and end2:
            answer_lst[idx1] = i # idx1 자리로 도착한 알파벳이 i에 해당
            break
        if min1<min2:
            min0=min1
            idx1-=1
        else:
            min0=min2
            idx1+=1
        # print(idx1,min0)
        present = min0    

alp="abcdefghijklmnopqrstuvwxyz"
for i in range(k):
    print(alp[answer_lst[i]],end=' ')
    
        

        
        