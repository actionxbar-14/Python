


# Empty Dictionary :

contacts = { }

while True:
    print("____Contact Book App____")
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit')

    choice = input('Enter Your Choice : ')



    if choice == '1':
        name = input("Enter Your name:")
        if name in contacts:
            print(f"Contact name {name} already exists!")

        else:
            age = input("Enter age :")
            email = input("Enter Email :")
            mobile_no = input("Enter mobile_no : ")
            contacts[name] = {'age' : int(age) , 'email' : email , 'mobile_no' : mobile_no}
            print(f"Contact name {name} has been created succussfully!")




    elif choice == '2':
        name = input("Enter Your name:")
        if name in contacts:
            contact = contacts[name]
            print(f"Name : {name} , Age : {age} , Mobile_no. : {mobile_no}")

        else:
            print("Contact not found!")



    elif choice == '3':
        name = input("Enter name to update contact = ")
        if name in contacts:
            age = input("Enter updated age :")
            email = input("Enter updated email :")
            mobile = input("Enter updated mobile_no :")
            contacts[name] = {'age' : int(age) , 'email' : email , 'mobile' : mobile_no}
            print("contact updated succussfully!")

        else:
            print('Contact not found!')



    elif choice == '4':
        name = input('Enter contact name to delete : ')
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted succussfully!")

        else:
            print("Contact not found!")


    elif choice == '5':
        search_name = input('Enter contact name to search : ')
        found = False 
        for name , contact in contacts.items():
            if serach_name in name:
                print(f"Found - Name : {name} , Age : {age} , Mobile_no. : {mobile_no} , Email : {email}")
                found = True

        if not found:
            print("No Contact found with that name:")


    elif choice == '6':
        print(f"Total contacts in your book : {len(contacts)}")


    elif choice == '7':
        print("Closing the program....")
        break

    
    else:
        print("Invalid Input")

   