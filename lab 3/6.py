def process_items():
    """
    Function to process the user input and store unique items in a set and non-unique items in a nested tuple.

    Returns:
    - set:
        Set containing the unique items entered by the user.
    - tuple:
        Tuple containing the frequency of non-unique items entered by the user.
    """

    # Prompting the user to enter items separated by commas
    user_input = input("Please enter items separated by comma: ")

    # Splitting the user input into a list of items
    items = user_input.split(",")

    # Stripping whitespace from each item in the list
    items = [item.strip() for item in items]

    # Creating a set to store unique items
    unique_items = set()

    # Creating a dictionary to store the frequency of non-unique items
    frequency_dict = {}

    # Iterating over each item in the list
    for item in items:
        # Checking if the item is already in the unique_items set
        if item in unique_items:
            # If the item is already in the set, increment its frequency in the dictionary
            frequency_dict[item] = frequency_dict.get(item, 0) + 1
        else:
            # If the item is not in the set, add it to the set
            unique_items.add(item)

    # Converting the frequency dictionary into a nested tuple
    frequency_tuple = tuple(frequency_dict.items())

    return unique_items, frequency_tuple


# Example usage of the process_items function

# Prompting the user to choose a task
task = input("Please choose the task you want to perform (Enter items/Exit): ")

# Checking the user's choice
if task.lower() == "enter items":
    # Calling the process_items function to process the user input
    unique_items, frequency_tuple = process_items()

    # Printing the unique items
    print("Unique items:", unique_items)

    # Printing the tuple with the frequency of non-unique items
    print("Frequency tuple:", frequency_tuple)
elif task.lower() == "exit":
    # Exiting the program
    print("Exiting...")
else:
    # Invalid choice
    print("Invalid choice. Please choose a valid task.")