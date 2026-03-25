arr=list(map(int, input().split()))
c0=c1=c2=0
for i in arr:
    if i==0:
        c0+=1
    elif i==1:
        c1+=1
    else:
        c2+=1
print("0 "*c0+"1 "*c1+"2 "*c2)