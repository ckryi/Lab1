try:
    student1 = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2], 'final_grade': 70.25}
    student2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}

    students = {student['name']: {key: value for key, value in student.items() if key != 'name'} for student in [student1, student2]}

    print("students =", students)
except ValueError:
    print("Bad input")