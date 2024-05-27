from queue import Queue

patient_list = Queue()
current_patient_name = None

while True:
    print("Desk Manager - Patient Registration and Appointment System")
    print("1.Register patient")
    print("2.Remove Patient after Meeting Doctor")
    print("3.Display Patient Queue")
    print("4.Exit")

    choice = int(input("Enter your choice (just enter the option number): "))
    if choice == 1:
        name = input("Enter Patient name: ")
        patient_list.put(name)
        current_patient_name = name
        print(f"Patient {name} regitered")

    elif choice == 2:
        patient_list.get()
        print(f"Patient {patient_list} removed after meeting the doctor")
    elif choice == 3:
        print("Current Patient Queue: ")
        print(patient_list.queue)
    elif choice == 4:
        print("Exiting program...")
    else:
        print("Invalid Input")