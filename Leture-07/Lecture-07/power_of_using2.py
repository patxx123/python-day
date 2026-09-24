attendance_week = [
    ["Alice", "Bob", "Charlie", "David"],
    ["Alice", "Charlie", "David"],
    ["Alice", "Bob", "David"],
    ["Alice", "David", "Eva"],
    ["Bob", "Charlie", "David"]
]

attendance_set = [set(day) for day in attendance_week]
print(attendance_set) 

attendence_sets = [
    {"Alice", "Bob", "Charlie",},
    {"Alice", "David", "Charlie"},
    {"Bob", "David", "Eva"},
]

present_every_day = set.intersection(*attendence_sets)
print("Present_every_day:" , present_every_day)

all_students = set.union(*attendence_sets)
absent_at_least_one_day = all_students - present_every_day
print("Absent_at_least_one_day:", absent_at_least_one_day)

first_day_present = attendence_sets[0]
last_day_present = attendence_sets[-1]
first_day_but_not_last_day = list(first_day_present - last_day_present)
print("Present on the first day but not on the last day:", first_day_but_not_last_day)

unique_students_count = len(all_students)
print("Total unique students:", unique_students_count)