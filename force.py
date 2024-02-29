print("Newton's second law of Motion")
print("Select the missing value:")
print("1. Mass(m)")
print("2. Acceleration (a)")
print("3. Force (f)")
missing_value_choice = input("Enter the option number for the missing value:")
if missing_value_choice == "1":
    a = float(input("Enter acceleration (a):"))
    f = float(input("Enter force (F):"))
    m = f / a
    print(f"Mass (m) = {m}")

elif missing_value_choice =="2":
    m = float(input("Enter mass (m):"))
    f= float(input("Enter force (F):"))
    a = f / m
    print(f"Acceleration (a) = {a}")

elif missing_value_choice == "3":
    m= float(input("Enter mass (m):"))
    a= float(input("Enter force (a):"))
    f= m * a 
    print (f"Force (F) = {f}" )

else:
    print("Invalid option selected for the missing value.")