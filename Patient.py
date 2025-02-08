from Person import Person

class Patient(Person):
    
    patient_count = 0

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            postcode (string): postcode of the patient
        """
        super().__init__(first_name, surname)  # Inherit from Person class
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms
        self.__doctor = 'None'  # Initialize with 'None' until a doctor is linked
        Patient.patient_count += 1

    def get_age(self):
        """Returns the age of the patient"""
        return self.__age  # Add this method to fix the error

    def get_mobile(self):
        """Returns the mobile number of the patient"""
        return self.__mobile  
    
    def set_doctor(self, doctor_name):
        self.__doctor = doctor_name

    def get_postcode(self):
        """Returns the postcode of the patient"""
        return self.__postcode 
    
    def get_symptoms(self):
        """Returns the symptoms of the patient"""
        return self.__symptoms 

    def get_doctor(self):
        """Returns the name of the doctor linked to this patient"""
        return self.__doctor

    def link(self, doctor):
        """Links a doctor to this patient
        
        Args:
            doctor (Doctor): the doctor object
        """
        self.__doctor = doctor.full_name()

    def print_symptoms(self):
        """Prints all the symptoms"""
        print(f"Symptoms for {self.full_name()}:")
        if self.__symptoms:
            for symptom in self.__symptoms:
                print(f"- {symptom}")
        else:
            print("No symptoms recorded.")

    def __str__(self):
        symptoms_str = ', '.join(self.__symptoms)
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{symptoms_str:^30}'
