def get_prime_numbers(n):

    prime_numbers = []

    for num in range(2, n + 1):
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(num)

    return prime_numbers

n = 100
result = get_prime_numbers(n)
print(result)