def get_date_in_format(date):

    year, month, day = date.split(".")

    formatted_date = f"{day}.{month}.{year}"

    return formatted_date

date_input = "2023.10.23"
formatted_date_output = get_date_in_format(date_input)
print(formatted_date_output)