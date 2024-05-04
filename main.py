from services.services import *
from students.students import *

create_students()

highest_student = highest_level_students(objs, level)
smallest_student = smallest_level_students(objs, level)
display_all_students = display_students(objs)

while True:
    input_field = input("Welcome to our students application!\nGive a number to start\nPress 1! Display All\n"
                        "Press 2! Mesos oros Hlikias\nPress 3! low lvl mathites"
                        "\nPress 4! high lvl mathites \nPress 5! exit : ")
    if input_field == "1":
        if display_all_students:
            for student in display_all_students:
                print(f"{student}\n")
    elif input_field == "2":
        mesos_oros_hlikias = print(f"O mesos oros hlikias twn mathitwn einai : {average_age(age)}\n")
    elif input_field == "3":
        if smallest_student:
            print(f"Oi mathites me to ligotero lvl({smallest_lvl(level)}) einai:")
            for student in smallest_student:
                print(f"{student}\n")
    elif input_field == "4":
        if highest_student:
            print(f"Oi mathites me to megalitero lvl({highest_lvl(level)}) einai:")
            for student in highest_student:
                print(f"{student}\n")
    elif input_field == "5":
        break









