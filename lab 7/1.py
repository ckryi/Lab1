def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "text1.txt"
read_text_file(file_name)
