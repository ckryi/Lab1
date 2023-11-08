import math
try:
    def find_perfect_squares(numbers):

        perfect_squares = []

        for num in numbers:
            if math.isqrt(num) ** 2 == num:
                perfect_squares.append(num)

        return perfect_squares
except ValueError:
    print("Bad Input")

input_numbers = [4, 25, 81, 32, 71]
perfect_squares_list = find_perfect_squares(input_numbers)
print(perfect_squares_list)