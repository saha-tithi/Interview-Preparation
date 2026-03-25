s1=input()
s2=input()
if len(s1)!=len(s2):
    print("NO")
else:
    freq={}
    for ch in s1:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for ch in s2:
        if ch in freq:
            freq[ch]-=1
        else:
            print("NO")
            break
    else:
        check=True
        for val in freq.values():
            if val!=0:
                check=False
                break
        if check:
            print("YES")
        else:
            print("NO")