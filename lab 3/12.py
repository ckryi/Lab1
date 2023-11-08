try:
    N = int(input())

    if N <= 1:
        print("No prime numbers in this range.")
    else:

        for num in range(2, N + 1):
            is_prime = True

            for divisor in range(2, num):
                if num % divisor == 0:
                    is_prime = False
                    break

            if is_prime:
                print(num)

except ValueError:
    print("Bad input")