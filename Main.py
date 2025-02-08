# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main(admin):
    doctors = [
        Doctor('John', 'Smith', 'Internal Med.'),
        Doctor('Jone', 'Smith', 'Pediatrics'),
        Doctor('Jone', 'Carlos', 'Cardiology')
    ]

    patients = [
        Patient('Sara', 'Smith', 20, '07012345678', 'B1 234', ['Fever', 'Cough', 'Headache']),
        Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB', ['Headache', 'Dizziness', 'Nausea', 'Sore Throat']),
        Patient('David', 'Smith', 15, '07123456789', 'C1 ABC', ['Sore throat', 'Runny nose', 'Cough', 'Constipation'])
    ]

    discharged_patients = []
    needs_relogin = False 

    
    while True:
        if admin.login():
            running = True  
            break
        else:
            print('Incorrect username or password.')

    while running:
        
        if needs_relogin:
            print("Admin details updated. Please log in again.")
            while True:
                if admin.login():
                    needs_relogin = False 
                    break
                else:
                    print('Incorrect username or password.')

        # Print the menu
        print('\nChoose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Add a patient')
        print(' 3- Discharge patients')
        print(' 4- View patient details')
        print(' 5- View discharged patient')
        print(' 6- Assign doctor to a patient')
        print(' 7- Update admin details')
        print(' 8- Get Management Report')
        print(' 9- Quit')

        # Get the option
        op = input('Option: ')

        if op == '1':
            admin.doctor_management(doctors)
        
        elif op == '2':
            admin.add_patient(patients)
        
        elif op == '3':
            while True:
                op = input('Do you want to discharge a patient (Y/N): ').lower()
                if op == 'yes' or op == 'y':
                    admin.discharge(patients, discharged_patients)
                elif op == 'no' or op == 'n':
                    break
                else:
                    print('Please answer by yes or no.')
        
        elif op == '4':
            admin.view_patient(patients, doctors)
        
        elif op == '5':
            admin.view_discharge(discharged_patients)
        
        elif op == '6':
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '7':
            if admin.update_details():
                needs_relogin = True  
                
                
        elif op == '8':
            admin.get_management_report(doctors, patients)
        
        elif op == '9':
            print("Exiting the system. Goodbye!")
            running = False 

        else:
            print('Invalid option. Try again')

if __name__ == '__main__':
    admin = Admin('admin', '123', 'B1 1AB')  # Username is 'admin', password is '123'
    while True:
        main(admin)  
