
def calculate_equation_result(X, N):
    result = 0
    
    for i in range(0, N+1, 2):
        result += X ** i
    
    return result


X, N = map(int, input().split())


result = calculate_equation_result(X, N)
print(result-1)
