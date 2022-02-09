class Patient:
    
    def __init__(self, name, id_no, age, dob = None):   #default value so that you don't need to use a variable
    
    #Variable belongs to the class, as opposed to local env
    
        self.name = name
        self.id = id_no
        self.age = age
        self.tests = []
        
    def __repr__(self) #Self must be a variable for all class methods
        return "Patient: {}, {}".format(self.name, self.id)
        
    def output_patient(self):
        outstr = "Name: {}\n".format(self.name)
        outstr += "Age: {}\n".format(self.id)
        outstr += "Age: {}\n".format(self.age)
    
    
        
def class_work():
    x = Patient         #assigning the class to the variable x
    y = Patient()       #creates an instance of the class !!! (__main__.Patient object)
    y.name = "Ann Ables"

def add_patient(name, id_no, age):

    # Each patient entry is a dictionary
    
    # new_patient = {"name": name, 
                    # "id": id_no, 
                    # "age": age, 
                    # "tests": []}   #4th element list of tests
                    
    
    new_patient = Patient(name, id_no, age)
    return new_patient
    
def output_database(db):
    for patient in db:
        output_patient(patient)
        
def find_patient(db, id_no):
    for patient in db:


def add_test(db, id_no, test_name, test_res):
    patient = 
   
def main():
    db = []
    x = add_patient("AA", 340, 40)
    db.append(x)
    print(db)
    
    found_patient = find_patient(db, 111)   ##Returns patient object, self-type variable
    print(found_patient.output_patient)     ##calls method on patient to format into correct string
    
    ## Whats the difference between a class method and a code function (where in file)
    
    return db

if __name__ == "__main__":
    main()

