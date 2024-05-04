from students.students import Students

f_name = ["Giannis", "Maria", "Kwstas", "Eleni", "Nikos", "Antwnhs", "Aggelikh", "Dimitris"]
l_name = ["Papadopoulos", "Karagianni", "Dhmitrioy", "Papanikolaou", "Andreou", "Mixahlidis", "Papadaki", "Kontogiannis"]
age = [15, 16, 14, 15, 17, 15, 14, 16]
level = [2, 3, 1, 2, 3, 2, 1, 3]

objs = list()

def create_students():

    for f, l, a, le in zip(f_name, l_name, age, level):
        student = Students(f, l, a, le)
        objs.append(student)
def display_students(objs):
    display_all_students = [(f"Onomateponimo: {obj.f_name} {obj.l_name}\nHlikia: {obj.age}\nEpipedo: {obj.level}\n")for obj in objs]
    return display_all_students

def average_age(age):
    return sum(age) / len(age)

def highest_level_students(objs, level):
    highest = max(level)
    highest_students = [(f"Mathitis: {obj.f_name} {obj.l_name}") for obj in objs if obj.level == highest]
    return highest_students

def highest_lvl(level):
    highest = max(level)
    return highest

def smallest_level_students(objs, level):
    smallest = min(level)
    smallest_students = [(f"Mathitis: {obj.f_name} {obj.l_name}") for obj in objs if obj.level == smallest]
    return smallest_students

def smallest_lvl(level):
    smallest = min(level)
    return smallest








