T=int(input())
for _ in range(T):
    x,y= map(int,input().split())
    odd_sum=0
    if x>y:
        x=y
        y=x
   
    for i in range(x+1,y):
        if i%2==1:
            odd_sum=odd_sum+i

    print(odd_sum)
