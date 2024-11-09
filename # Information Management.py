# Information Management 
information = {}

while True:
    print("1. Add information")
    print("2. Retrieve information")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")
        information[key] = value
        print("Information added successfully!")
    elif choice == "2":
        key = input("Enter key to retrieve information: ")
        if key in information:
            print("Value:", information[key])
        else:
            print("Key not found!")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")