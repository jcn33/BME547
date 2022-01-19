def interface():
    print("My Program")
    key = True
    while key:
        print("Options:")
        print("9 - Quit")
        print("8 - Analyze HDL")
        choice = input("Enter your choice: ")
        if choice=='9':
            key = False
        if choice=='8':
            HDL_Driver()
            key = False
    return
    
def accept_input(test):
    entry = input("Enter the {} test result: ".format(test))
    return int(entry)
    
def analyze_HDL(value):
    if value >= 190:
        answer = "Very High"
    elif 190 > value >= 160:
        answer = "High"
    elif 160 > value >= 130:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer
    
def analyze_LDL(value):
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
    
interface()

