# Function to generate the first N Fibonacci numbers
def generate_fibonacci(N):
    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers
    
    for i in range(2, N):
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)
    
    return fibonacci_sequence

# Read the value of N
N = int(input())

# Generate and print the first N Fibonacci numbers
fibonacci_sequence = generate_fibonacci(N)
print(" ".join(map(str, fibonacci_sequence)))
