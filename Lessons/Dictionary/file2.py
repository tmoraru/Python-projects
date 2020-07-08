def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values())  / len(value)
    else:
        the_mean = sum(value) / len(value)
   
    return the_mean

monday_temperatures = [8.9, 3.5, 3.2]
student_grades = {"Ma": 9.1, "Sim": 9.3, "GO": 9.4}
print(mean(student_grades))