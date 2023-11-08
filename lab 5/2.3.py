try:
    student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
    rate = {'Adam': 6}

    if student['name'] in rate and rate[student['name']] >= 4:
        assignment_average = sum(student['assignment']) / len(student['assignment'])
        lab_average = sum(student['lab']) / len(student['lab'])
        test_average = sum(student['test']) / len(student['test'])
        final_grade = 0.3 * assignment_average + 0.5 * lab_average + 0.2 * test_average
        student['final_grade'] = final_grade
    else:
        student['final_grade'] = 0

    print("student =", student)
except ValueError:
    print("Bad input")