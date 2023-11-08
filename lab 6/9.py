from datetime import datetime

def get_difference_between_dates(date1, date2):

    try:
        date1_obj = datetime.strptime(date1, '%Y-%m-%d')
        date2_obj = datetime.strptime(date2, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Bad Input")

    if date2_obj < date1_obj:
        raise ValueError("Bad Input")
    else:
        difference = (date2_obj - date1_obj).days

    return difference

date1 = '2022-01-01'
date2 = '2022-01-10'
difference = get_difference_between_dates(date1, date2)
print(f"The difference between {date1} and {date2} is {difference} days.")