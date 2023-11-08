def is_prime(n):

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def get_prime_numbers_in_list(lst):

    prime_numbers = []

    for num in lst:
        if is_prime(num):
            prime_numbers.append(num)

    return prime_numbers


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89,
99]
prime_numbers_list = get_prime_numbers_in_list(input_list)
print(prime_numbers_list)