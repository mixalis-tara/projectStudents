from students.student import Student

students_dict = {}

def create_students_from_file():
    try:
        with open("Student.txt", encoding="utf-8") as infile:
            for line in infile:
                listfields = line.strip().split()
                if len(listfields) == 4:
                    f, l, a, le = listfields

                    a = int(a)
                    le = int(le)

                    student = Student(f, l, a, le)

                    key = f"{f}_{l}"
                    students_dict[key] = student
                else:
                    print(f"Ignoring line: {line.strip()}")
        return students_dict
    except FileNotFoundError:
        print("File not found or cannot be opened.")


def display_students(students_dict):
    display_all_students = []
    for key, student in students_dict.items():
        display_all_students.append(
            f"Onomateponimo: {student.f_name} {student.l_name}\nHlikia: {student.age}\nEpipedo: {student.level}\n"
        )
    return display_all_students

def average_age(students_dict):
    ages = [student.age for student in students_dict.values()]

    if ages:
        avg_age = sum(ages) / len(ages)
        return avg_age
    else:
        return 0

#
def highest_level_students(students_dict):
    level = [student.level for student in students_dict.values()]
    display_highest_level_students = []
    highest = max(level)
    for key, student in students_dict.items():
        if student.level == highest:
            display_highest_level_students.append (
                f"Mathitis: {student.f_name} {student.l_name}"
            )
    return display_highest_level_students
#
def highest_lvl(students_dict):
    level = [student.level for student in students_dict.values()]
    highest = max(level)
    return highest
#
def smallest_level_students(students_dict):
    level = [student.level for student in students_dict.values()]
    display_smallest_level_students = []
    smallest = min(level)
    for key, student in students_dict.items():
        if student.level == smallest:
            display_smallest_level_students.append(
                f"Mathitis: {student.f_name} {student.l_name}"
            )
    return display_smallest_level_students
#
def smallest_lvl(students_dict):
    level = [student.level for student in students_dict.values()]
    smallest = min(level)
    return smallest








