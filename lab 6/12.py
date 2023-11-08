try:
    def sort_by_price(shopping_list):

        sorted_list = sorted(shopping_list, key=lambda x: x['price'])

        return sorted_list


    shopping_list = [
        {"name": "Apple", "price": 100},
        {"name": "Banana", "price": 50},
        {"name": "Orange", "price": 20}
    ]

    sorted_shopping_list = sort_by_price(shopping_list)
except ValueError:
    print("Bad Input")

print("Sorted Shopping List:")
for item in sorted_shopping_list:
    print(f"name: {item['name']}, price: {item['price']}")