#Initialize empty lists and dictonary
students_list=[]
students_dict={}

#Add student information 
name = input("Enter student's name: ")
age = input("Enter student's age: ")
grade = input("Enter student's grade: ")
students_list.append(name)
students_dict[name] = {"age, grade" : grade}
print("Student informaion added sucessfully!")
print(students_dict.items()) 

#Search for a student by name
search_name = input("Enter the name of the student to search or simply enter to skip: ")
if search_name in students_list:
    info = students_dict[search_name] 
    print(f"Name: { }")