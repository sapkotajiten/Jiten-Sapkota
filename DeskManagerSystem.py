from queue import Queue

def register_patient(queue):
    patient_name = input("Enter patient name: ")
    queue.put(patient_name)
    print("Patient", patient_name, "registered.")

def remove_patient(queue):
    if queue.empty():
        print("No patients in the queue.")
    else:
        patient_name = queue.get()
        print("Patient", patient_name, "removed after meeting the doctor.")

def display_patient_queue(queue):
    if queue.empty():
        print("No patients in the queue.")
    else:
        print("Current patient queue:")
        for index, patient in enumerate(list(queue.queue), start=1):
            print(index, ".", patient)

def main():
    patient_queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_patient(patient_queue)
        elif choice == '2':
            remove_patient(patient_queue)
        elif choice == '3':
            display_patient_queue(patient_queue)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()







































































