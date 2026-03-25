a,b=map(int, input().split())
for num in range(a,b+1):
    if num>1:
        is_p=True
        for i in range(2,num):
            if num%i==0:
                is_p=False
                break
        if is_p:
            print(num,end=",")
            
