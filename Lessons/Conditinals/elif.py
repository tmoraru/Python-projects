def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)

    else:
        the_mean = sum(value) / len(value)

    return the_mean

monday_temperatures = [4, 3, 5 ]
student_grades = {"Tanya": 9.5, "Marry": 9.5, "Ana": 9.4}

print(mean(student_grades))