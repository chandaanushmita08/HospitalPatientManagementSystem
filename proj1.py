# Hospital Patient Management System

patients = []

def add_patient():
    print("\n--- Add Patient ---")

    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    disease = input("Enter Disease/Condition: ")
    doctor = input("Enter Doctor Name: ")

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease,
        "doctor": doctor
    }

    patients.append(patient)

    print("\nPatient added successfully!")


def view_patients():
    print("\n--- Patient Records ---")

    if len(patients) == 0:
        print("No patient records found.")
        return

    for patient in patients:
        print("\nPatient ID:", patient["id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Disease/Condition:", patient["disease"])
        print("Doctor:", patient["doctor"])


def search_patient():
    print("\n--- Search Patient ---")

    patient_id = input("Enter Patient ID: ")

    for patient in patients:
        if patient["id"] == patient_id:
            print("\nPatient Found!")
            print("Patient ID:", patient["id"])
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Disease/Condition:", patient["disease"])
            print("Doctor:", patient["doctor"])
            return

    print("Patient not found.")


def delete_patient():
    print("\n--- Delete Patient ---")

    patient_id = input("Enter Patient ID: ")

    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)
            print("Patient record deleted successfully!")
            return

    print("Patient not found.")


def main():
    while True:
        print("\n==============================")
        print(" HOSPITAL PATIENT MANAGEMENT")
        print("==============================")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            delete_patient()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
