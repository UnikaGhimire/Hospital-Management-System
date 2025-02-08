from Doctor import Doctor
from Patient import Patient
import matplotlib.pyplot as plt
 

class Admin:
    
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        self.__username = username
        self.__password = password
        self.__address =  address
    
    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_address(self):
        return self.__address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')
        
        if self.__username == username and self.__password == password:
            print("Login successful!")
            return True
        else:
            return False
       
    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        
        return self.__first_name, self.__surname, self.__speciality
        

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        
        op = input('Option: ') 


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name = input("Enter first name of the doctor: ")
            surname = input("Enter surname of the doctor: ")
            speciality = input("Enter speciality of the doctor: ")
            
            
            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    name_exists =  True
                    print('Name already exists.')
                    break
                    
                    #ToDo5
                     # save time and end the loop

            if name_exists:
                return  # Stop further processing if name exists

        # Add the doctor to the list of doctors
            new_doctor = Doctor(first_name, surname, speciality)
            doctors.append(new_doctor)
                                                         # ... to the list of doctors
            print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            for doctor in doctors:
                print(doctor)
                

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    if self.find_index(index, doctors):
                        doctor = doctors[index]  # Assign the doctor object
                        break
                    else:
                        print("Doctor not found")
                        return

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')
                    return

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            update_op = input('Input: ') # make the user input lowercase
            
            if update_op == '1':
            # Update first name
                new_first_name = input(f"Enter new first name (current: {doctor.get_first_name()}): ")
                doctor.set_first_name(new_first_name)
                print(f"Doctor's first name updated to {new_first_name}")

            elif update_op == '2':
            # Update surname
                new_surname = input(f"Enter new surname (current: {doctor.get_surname()}): ")
                doctor.set_surname(new_surname)
                print(f"Doctor's surname updated to {new_surname}")

            elif update_op == '3':
            # Update speciality
                new_speciality = input(f"Enter new speciality (current: {doctor.get_speciality()}): ")
                doctor.set_speciality(new_speciality)
                print(f"Doctor's speciality updated to {new_speciality}")

            else:
                print('Invalid option. Please select a valid option.')

           
                

    # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            
            try:
                # Convert the input to an integer (doctor ID)
                doctor_index = int(doctor_index) - 1  # Adjust for 0-based index

                # Check if the ID exists in the list
                if self.find_index(doctor_index, doctors):
                    # Confirm before deleting
                    confirm = input(f"Are you sure you want to delete {doctors[doctor_index].get_first_name()} {doctors[doctor_index].get_surname()}? (yes/no): ").lower()
                    if confirm == 'yes':
                        # Delete the doctor from the list
                        deleted_doctor = doctors.pop(doctor_index)
                        print(f"Doctor {deleted_doctor.get_first_name()} {deleted_doctor.get_surname()} deleted successfully.")
                    else:
                        print("Doctor deletion cancelled.")
                else:
                    print("Doctor not found.")

            except ValueError:
                print("The ID entered is incorrect. Please enter a valid integer.")
    
    


    def add_patient(self, patients):
        
        first_name = input("Enter patient's first name: ")
        surname = input("Enter patient's surname: ")
        age = int(input("Enter patient's age: "))
        mobile = input("Enter patient's mobile number: ")
        postcode = input("Enter patient's postcode: ")
        symptoms = input("Enter patient's symptoms (separate by commas): ").split(",")
        
        with open("patients.txt",'a') as file:
                first_name = input("Enter patient's first name: ")
                surname = input("Enter patient's surname: ")
                age = int(input("Enter patient's age: "))
                mobile = input("Enter patient's mobile number: ")
                postcode = input("Enter patient's postcode: ")
                symptoms = input("Enter patient's symptoms (separate by commas): ").split(",")

                file.write("\n")
                file.write(
                    f"{first_name},{surname},{age},{mobile},{postcode},None,{','.join(symptoms)}"
                    )


                
        patients = self.load_patient_file("patient.txt")   
        print("Patient added successfully.")
            



    def view_patient(self, patients, doctors):
        print(' 1- View all patient details')
        print(' 2- View patients from the same family')
        print(' 3- View patients under a specific doctor')
        print(' 4- Relocate Patient from one doctor to another')
        
        
        ch = input("Enter your choice: ")
        
        if ch == '1':
            print("-----Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            self.view(patients)
            
        
        
        elif ch == '2':
            surname = input("\nEnter surname: ")
            matching_patients = []
            
            for p in patients:
                if p.get_surname().lower() == surname.lower():
                    matching_patients.append(p)
            
            if matching_patients:
                print(f"\nPatients in {surname} family:")
                print("ID | Name | Doctor | Age | Phone | Postcode")
                id = 0
                for p in matching_patients:
                    id = id+1
                    print("\n")
                    print(f"{id} | {p.full_name()} | {p.get_doctor()} | {p.get_age()} | {p.get_mobile()} | {p.get_postcode()}")
            else:
                print("No patients found with that family name.")
                
        elif ch == '3':
            
            print("\nAvailable Doctors:")
            print("Name                | Specialty")
            
            for doctor in doctors:
                print(doctor.full_name(),         doctor.get_speciality())  

            # Get doctor details from the user
            doc_first = input("\nEnter doctor's first name: ")
            doc_last = input("Enter doctor's last name: ")

            # Find the doctor in the list
            doctor = None  
            for d in doctors:
                if d.get_first_name().lower() == doc_first.lower() and d.get_surname().lower() == doc_last.lower():
                    doctor = d
                    break

            if doctor:
                # List patients assigned to the doctor
                patients_under_doctor = []
                doctor_full_name = doctor.full_name()  # Get the full name correctly
                
                for p in patients:
                    if p.get_doctor().lower() == doctor_full_name.lower():
                        patients_under_doctor.append(p)

                if patients_under_doctor:
                    print(f"\nPatients under Dr. {doctor_full_name}:")
                    print("Name")
                    print("-----")
                    for p in patients_under_doctor:
                        print(p.full_name())  # Print only the name of each patient
                else:
                    print(f"No patients found under Dr. {doctor_full_name}")
            else:
                print("Doctor not found")

        elif ch == '4':
            pass
        
        else:
            print("Invalid choice.")
    
    
        

        

    def assign_doctor_to_patient(self, patients, doctors):
        print("-----Assign Patient-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            patient_index = int(patient_index) - 1

            if patient_index not in range(len(patients)):
                print('The ID entered was not found.')
                return  
 
        except ValueError:
            print('The ID entered is incorrect.')
            return  

        selected_patient = patients[patient_index]
        previous_doctor = selected_patient.get_doctor()  
        # Check if the patient already has a doctor
        if previous_doctor and previous_doctor != "None":
            relocate = input(f"Patient {selected_patient.full_name()} is already assigned to Dr. {previous_doctor}. Do you want to relocate them? (yes/no): ").strip().lower()
            
            if relocate == "no":
                print("No changes made.")
                return  

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        selected_patient.print_symptoms()  # Print patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        
        doctor_index = input('Please enter the doctor ID: ')

        try:
            doctor_index = int(doctor_index) - 1

            if self.find_index(doctor_index, doctors) != False:
                selected_doctor = doctors[doctor_index]

                # Assign the new doctor
                selected_patient.link(selected_doctor)  # Pass the Doctor object directly
                selected_doctor.add_appointment()

                if previous_doctor:  
                    print(f"Patient {selected_patient.full_name()}'s doctor has been updated from Dr. {previous_doctor} to Dr. {selected_doctor.full_name()}.")
                else:
                    print(f'Patient {selected_patient.full_name()} is now assigned to Dr. {selected_doctor.full_name()}.')

                # Update the file with the new doctor assignment
                with open("patients.txt", "w") as file:
                    file.write('Name | Surname | Doctor | Age | Mobile | Postcode | Symptoms\n')
                    for patient in patients:
                        file.write(f'{patient.get_first_name()} {patient.get_surname()} | {patient.get_doctor()} | {patient.get_age()} | {patient.get_mobile()} | {patient.get_postcode()} | {", ".join(patient.get_symptoms())}\n')

            else:
                print('The ID entered was not found.')

        except ValueError:
            print('The ID entered is incorrect.')


    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done.
        Args:
            patients (list<Patients>): the list of all the active patients
            discharged_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        try:
            patient_index = int(input("Enter patient ID: ")) - 1  
            if 0 <= patient_index < len(patients):  
                discharged_patient = patients.pop(patient_index)  # Remove patient from active list
                discharged_patients.append(discharged_patient)  # Add patient to discharged list
                print("Discharge is successful.")

                # Update the patients.txt file
                self.update_patients_file(patients)

            else:
                print("Invalid ID. Patient not found.")
                return None
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def update_patients_file(self, patients):
        # Read the existing content of the file
        with open("patients.txt", "r") as file:
            lines = file.readlines()

        # Modify the list of patients and write it back to the file
        with open("patients.txt", "w") as file:
            file.write('Name | Surname | Doctor | Age | Mobile | Postcode | Symptoms\n')  
            i = 0
            for patient in patients:
                i = i + 1
                file.write(f"{i} | {patient.full_name()} | {patient.get_doctor()} | {patient.get_age()} | {patient.get_mobile()} | {patient.get_postcode()} | {', '.join(patient.get_symptoms())}\n")



    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)
    
    
    def get_management_report(self,doctors,patients):
            print("-----Management Reports-----")
            print('Choose the operation:')
            print(' 1 - Total number of doctors in the system')
            print(' 2 - Total number of patients per doctor')
            print(' 3 - Total number of appointments per month per doctor')
            print(' 4 - Total number of patients based on the illness type.')
            op = input('Choose an option: ')
            
            try:
                if op =='1':
                    print('-------------Hospital Management System--------------')
                    print(f"The total number of doctors: {len(doctors)}")
                    
                elif op == '2':
                    print('-------------Hospital Management System--------------')
                    
                    for doctor in doctors:
                        totalPatients = doctor.get_total_patients()
                        print(f"{doctor.full_name()} has {totalPatients} patients")

                    # Create graph
                    doctor_names = [doctor.full_name() for doctor in doctors]  
                    total_patients = [doctor.get_total_patients() for doctor in doctors]  

                    plt.figure(figsize=(10, 6))
                    plt.bar(doctor_names, total_patients, color='skyblue')

                    # Adding labels and title
                    plt.xlabel('Doctor')
                    plt.ylabel('Total Patients')
                    plt.title('Total Patients per Doctor')

                    # Rotating x-axis labels for better readability
                    plt.xticks(rotation=45, ha='right')

                    # Displaying the plot
                    plt.tight_layout()
                    plt.show()

                
                elif op == '3':
                    print('-------------Hospital Management System--------------')
                    for doctor in doctors:
                        total_appointments = doctor.get_total_appointments()  # Get appointments from the Doctor class
                        print(f"{doctor.full_name()} has {total_appointments} appointments this month")
                    
                    # Create graph
                    doctor_names = [doctor.full_name() for doctor in doctors]
                    total_appointments = [doctor.get_total_appointments() for doctor in doctors]

                    plt.figure(figsize=(8, 5))
                    plt.bar(doctor_names, total_appointments, color='orange')
                    plt.xlabel('Doctors')
                    plt.ylabel('Total Appointments')
                    plt.title('Total Appointments per Doctor')
                    plt.xticks(rotation=45, ha='right')
                    plt.tight_layout()
                    plt.show()


                elif op == '4':
                   
                    symptom_count = {}

                    for patient in patients:
                        
                        symptoms = patient.get_symptoms()

                        
                        for symptom in symptoms:
                            
                            if symptom in symptom_count:
                                symptom_count[symptom] += 1
                            
                            else:
                                symptom_count[symptom] = 1

                    # Print the count of patients for each symptom
                    for symptom, count in symptom_count.items():
                        print(symptom + ": " + str(count) + " patients")
                        
                    symptoms = list(symptom_count.keys())  # List of symptoms
                    counts = list(symptom_count.values())  # List of counts

                    # Create a bar graph
                    plt.bar(symptoms, counts, color='skyblue')

                    # Add labels and title to the graph
                    plt.xlabel('Symptoms')  # X-axis label
                    plt.ylabel('Number of Patients')  # Y-axis label
                    plt.title('Number of Patients per Symptom')  # Title of the graph

                    # Rotate x-axis labels for better readability
                    plt.xticks(rotation=45, ha='right')

                    # Display the plot
                    plt.tight_layout()  # Adjust layout to avoid overlap
                    plt.show()

                else:
                    print("Invalid Option")    
            except Exception as e:
                print(e)


        
        
        
        
    

    def update_details(self):
        """
        Allows the user to update and change username, password, and address.
        """

        try:
            print('Choose the field to be updated:')
            print(' 1 Username')
            print(' 2 Password')
            print(' 3 Address')
            op = int(input('Input: '))  

            if op == 1:
                username = input('Enter the new username: ')
                self.__username = username
                print("You have successfully changed the username.")
                return True

            elif op == 2:
                password = input('Enter the new password: ')
                if password == input('Enter the new password again: '):  # Checking password confirmation
                    self.__password = password
                    print("You have successfully changed the password.")
                    return True
                else:
                    print("Passwords do not match.")
                    return False

            elif op == 3:
                address = input('Enter the new address: ')
                self.__address = address
                print("You have successfully changed the address.")
                return True

            else:
                print("Invalid input. Please enter 1, 2, or 3.")
                return False

        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
