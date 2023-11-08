try:
    a = int(input())
    b = int(input())
    c = int(input())

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths should be positive.")
    
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Versatile")

except ValueError:
    print("Bad Input")

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')