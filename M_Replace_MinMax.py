N=input()
A=list(map(int, input().split()))
minimum= min(A)
maximum= max(A)
minimum_idx= A.index(minimum)
maximum_idx= A.index(maximum)
A[minimum_idx]=maximum
A[maximum_idx]=minimum

string_out= " ".join(map(str, A))
print(string_out)
