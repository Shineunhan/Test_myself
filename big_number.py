n,m,k = map(int,input().split())
li = list(map(int,input().split()))

li.sort()

max=li[n-1]
max2=li[n-2]

result = 0
if max==max2:
    print(max*m)
else:
    while True:
        for i in range(k):
            if m==0:
                break
            result+=max
            m-=1

        if m==0:
            break
        result+=max2
        m-=1
    print(result)

