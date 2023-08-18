def print_fibonacci(length):
    fibonacci_sequence = []

    if length > 0:
        fibonacci_sequence = [0, 1]

        for i in range(2, length):
            next_value = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
            fibonacci_sequence.append(next_value)

    print(fibonacci_sequence)
