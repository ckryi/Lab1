def get_number_of_days(month: int):
    if month < 1 or month > 12:
        raise ValueError("Bad Input")

    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return days_in_month[month]

try:
    month_number = int(input())
    days = get_number_of_days(month_number)
    print(days)
except ValueError:
    print("Bad Input")