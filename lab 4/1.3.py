try:
    tuple_A = (1, 2, 3, 4, 5, 6, 7)
    tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)
    
    half = len(tuple_A) // 2
    
    concatenated_tuple = tuple_A[:half] + tuple_B[half:]
    
    print(concatenated_tuple)

except ValueError:
    print("Bad Input")
