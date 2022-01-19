def interface():
    print("My Program")
    key = True
    while key:
        print("Options:")
        print("9 - Quit")
        print("8 - Analyze HDL")
        choice = input("Enter your choice: ")
        if choice=='9':
            key = FALSE
        if choice=='8':
            HDL_Driver
            key = FALSE
    return
    
def accept_input(test):
    entry = input("Enter the {} test result: ".format(test))
    return int(entry)
    
def analyze_input(value):
    if value >= 60
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
    status = analyze_input(HDL)
    output(status)
    
interface()

