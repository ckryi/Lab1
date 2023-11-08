try:
    student_name = "Adam"
    assignment = [82, 56, 44, 30]
    lab = [78.20, 77.20]
    test = [78, 77]

    student = {
        'name': student_name,
        'assignment': assignment,
        'test': test,
        'lab': lab
    }

    print("student =", student)

except ValueError:
    print("Bad input")