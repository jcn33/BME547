x = __name__                    #Special variable (starts and ends with _)
                                # = "__main__"
                                
from interface import analyze_HDL   #importing runs code
import interface as it              #__name__ variable in interface code = "interface"

#Can avoid complications with 
# if __name__ == "__main__"

def add_patient(name, id, age):
    patient = [name, id, age, []]
    return patient

def main():
    db = []
    x = add_patient("AA", 340, 40)
    
    #first item of db is a list
    #second item is another patient list
    # db[-1] = last item in list
    
    db.append(x)
    
    s = "abcdef"
    print(s[0:5:2])

if __name__ == "__main__":
    main()

