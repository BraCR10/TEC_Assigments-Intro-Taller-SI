def sumatoria(n):
    if n==0:
        return 0
    else:
        sum=0
        i=0
        while i<=n:
            sum+=i
            i+=1
        print(sum)
sumatoria(2)
def sumatoria(n):
    if n==0:
        return 0
    else:
        sum=0
        for i in range(n+1):
            sum+=i
        print(sum)
sumatoria(2)