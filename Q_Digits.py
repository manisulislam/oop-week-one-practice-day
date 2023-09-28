def print_digits_from_right_to_left(num):
    num_str = str(num)
    for i in range(len(num_str) - 1, -1, -1):
        print(num_str[i], end=' ')

T = int(input())
for _ in range(T):
    N = int(input())
    print_digits_from_right_to_left(N)
    print()
