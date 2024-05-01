from students.students import Students

f_name = ["Giannis", "Maria", "Kwstas"]
l_name = ["Papadopoulos", "Karagianni", "Dhmitrioy"]
age = [15, 16, 14]
level = [2, 3, 1]

objs = list()

def create_students():

    for f, l, a, le in zip(f_name, l_name, age, level):
        student = Students(f, l, a, le)
        objs.append(student)
def display_students():
    for obj in objs:
        print(f"Onomateponimo: {obj.f_name} {obj.l_name}\nHlikia: {obj.age}\nEpipedo: {obj.level}\n")

