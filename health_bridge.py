
patients = {}  
doctors = {} 
appointments = []  
medical_records = []  

# Function to register a new patient
def register_patient():
    patient_id = input("Enter Patient ID: ").strip()
    if patient_id in patients:
        print("Patient already registered.\n")
        return

    name = input("Enter Patient Name: ").strip()
    age = input("Enter Patient Age: ").strip()
    patients[patient_id] = {"name": name, "age": age}
    print(f"Patient '{name}' registered successfully.\n")

def register_doctor():
    doctor_id = input("Enter Doctor ID: ").strip()
    if doctor_id in doctors:
        print("Doctor already registered.\n")
        return

    name = input("Enter Doctor Name: ").strip()
    specialization = input("Enter Doctor Specialization: ").strip()
    doctors[doctor_id] = {"name": name, "specialization": specialization}
    print(f"Doctor '{name}' registered successfully.\n")

# Book an appointment for a patient
def book_appointment():
    patient_id = input("Enter Patient ID: ").strip()
    if patient_id not in patients:
        print("Patient not registered. Please register first.\n")
        return

    doctor_id = input("Enter Doctor ID: ").strip()
    if doctor_id not in doctors:
        print("Doctor not registered. Please register first.\n")
        return

    appointment_time = input("Enter Appointment Time (YYYY-MM-DD HH:MM): ").strip()
    appointment_id = len(appointments) + 1  

    appointments.append({
        "appointment_id": appointment_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "appointment_time": appointment_time
    })
    
    print(f"Appointment booked for {patients[patient_id]['name']} with Dr. {doctors[doctor_id]['name']} at {appointment_time}.\n")

# Add a medical record for a patient
def add_medical_record():
    appointment_id = int(input("Enter Appointment ID: ").strip())
    appointment = next((appt for appt in appointments if appt["appointment_id"] == appointment_id), None)

    if not appointment:
        print("Appointment not found.\n")
        return

    diagnosis = input("Enter Diagnosis: ").strip()
    treatment = input("Enter Treatment: ").strip()
    record_date = input("Enter Record Date (YYYY-MM-DD): ").strip()

    medical_records.append({
        "record_id": len(medical_records) + 1,
        "patient_id": appointment["patient_id"],
        "doctor_id": appointment["doctor_id"],
        "appointment_id": appointment_id,
        "diagnosis": diagnosis,
        "treatment": treatment,
        "record_date": record_date
    })

    print(f"Medical record for {patients[appointment['patient_id']]['name']} added successfully.\n")

# View the data stored in the system
def view_data():
    print("\n1. View Patients")
    print("2. View Doctors")
    print("3. View Appointments")
    print("4. View Medical Records")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("\nRegistered Patients:")
        for pid, info in patients.items():
            print(f"ID: {pid}, Name: {info['name']}, Age: {info['age']}")
    elif choice == "2":
        print("\nRegistered Doctors:")
        for did, info in doctors.items():
            print(f"ID: {did}, Name: {info['name']}, Specialization: {info['specialization']}")
    elif choice == "3":
        print("\nAppointments:")
        for appt in appointments:
            patient_name = patients[appt["patient_id"]]["name"]
            doctor_name = doctors[appt["doctor_id"]]["name"]
            print(f"Appointment ID: {appt['appointment_id']}, Patient: {patient_name}, Doctor: {doctor_name}, Time: {appt['appointment_time']}")
    elif choice == "4":
        print("\nMedical Records:")
        for record in medical_records:
            patient_name = patients[record["patient_id"]]["name"]
            doctor_name = doctors[record["doctor_id"]]["name"]
            print(f"Record ID: {record['record_id']}, Patient: {patient_name}, Doctor: {doctor_name}, Diagnosis: {record['diagnosis']}, Treatment: {record['treatment']}, Date: {record['record_date']}")
    else:
        print("Invalid choice.\n")

# Main function to run the program
def main():
    while True:
        print("\nHealth Bridge - Medical Appointment System")
        print("1. Register Patient")
        print("2. Register Doctor")
        print("3. Book Appointment")
        print("4. Add Medical Record")
        print("5. View Data")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            register_patient()
        elif choice == "2":
            register_doctor()
        elif choice == "3":
            book_appointment()
        elif choice == "4":
            add_medical_record()
        elif choice == "5":
            view_data()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

