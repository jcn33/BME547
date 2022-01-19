def interface():
    print("My Program")
    key = True
    while key:
        print("Options:")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            key = FALSE
    return
    
def accept_input(test):
    entry = input("Enter the {} test result: ".format(test))
    return int(entry)
    
    
accept_input()
interface()