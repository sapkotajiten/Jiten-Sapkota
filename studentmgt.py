students_list = []
students_dict = {}

name = input("Enter the name of a student: ")
age = int(input("Enter the age of a student: "))
grade = input("Enter the grade of a student: ")

students_list.append(name)
students_dict[name] = {"age": age, "grade": grade}
print("Student information added successfully!")
print(students_dict)

search_std = input("Enter the name of the student to search or simply press enter to skip: ")
if search_std in students_list:
    print(f"Name: {search_std}, Age: {students_dict[search_std]['age']}, Grade: {students_dict[search_std]['grade']}")
else:
    print("Student not found!")

remove_std = input("Enter the name of the student to remove or simply enter the skip: ")
if remove_std in students_list:
    del students_dict [remove_std]
    students_list.remove(remove_std)
    print ("Student name removed successfully!")
    
else:
    print("Students not found")