num=int(input("Enter a number :"))
temp=num
sum=0
while(num>0):
    r=num%10
    sum=sum+(r*r*r)
    num=num//10
if(temp==sum):
    print("ARMSTRONG")
else:
    print("NOT  ARMSTRONG")