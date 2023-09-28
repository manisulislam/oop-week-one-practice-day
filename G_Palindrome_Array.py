N= int(input())
A= list(map(int, input().split()))
isPalindrome=True
for i in range(N//2):
    if A[i]!=A[N-1-i]:
        isPalindrome=False
        break
if isPalindrome:
    print("YES")
else:
    print("NO")

