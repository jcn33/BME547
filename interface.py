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
   
interface()