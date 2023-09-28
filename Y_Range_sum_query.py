N= int(input().split())
Q= int(input().split())
A= list(map(int,input().split()))
for i in range(Q):
    L= int(input().split())
    R= int(input().split())

for i in A[L:R]:
    sum=0
    sum=sum+i
    print(sum)
