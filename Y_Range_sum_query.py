# Read input
N, Q = map(int, input().split())
A = list(map(int, input().split()))

# Calculate the prefix sum
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

# Process queries
for _ in range(Q):
    L, R = map(int, input().split())
    
    # Calculate the sum from index L to R
    result = prefix_sum[R] - prefix_sum[L - 1]
    print(result)
