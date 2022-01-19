def interface():
    print("My Program")
    key = True
    while key:
        print("Options:")
        print("9 - Quit")
        print("8 - Analyze HDL")
        print("7 - Analyze LDL")
        print("6 - Analyze Total Cholesterol")
        choice = input("Enter your choice: ")
        if choice=='9':
            key = False
        if choice=='8':
            HDL_Driver()
            key = False
        if choice=='7':
            LDL_Driver()
            key = False
        if choice=='6':
            Total_Driver()
            key = False
    return
    
def accept_input(test):
    entry = input("Enter the {} test result: ".format(test))
    return int(entry)
    
def analyze_TC(value):
    if value < 200:
        answer = "Normal"
    elif 240 > value >= 200:
        answer = "Borderline High"
    else:
        answer = "High"
    return answer
   
def analyze_LDL(value):
    if value >= 190:
        answer = "Very High"
    elif 190 > value >= 160:
        answer = "High"
    elif 160 > value >= 130:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer

    
def analyze_HDL(value):
    if value >= 60:
        answer = "Normal"
    elif 60 > value >= 40:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer
    
def output(status):
    print(status)
    
def HDL_Driver():
    HDL = accept_input("HDL")
    status = analyze_HDL(HDL)
    output(status)

def LDL_Driver():
    LDL = accept_input("LDL")
    status = analyze_LDL(LDL)
    output(status)
    
def Total_Driver():
    Total = accept_input("Total Cholesterol")
    status = analyze_TC(Total)
    output(status)
    
interface()

