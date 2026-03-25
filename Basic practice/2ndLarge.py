arr=list(map(int, input().split()))
first=second=-999999
for num in arr:
    if num>first:
        second=first
        first=num
    elif num>second and num!=first:
        second=num
print(second)