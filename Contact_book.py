import pickle
global Contacts
Contacts={}

def pic():
    global Contacts
    with open('contacts.txt', 'wb') as fh:
        pickle.dump(Contacts, fh)

def unpic():
    global Contacts
    pickle_off = open ("contacts.txt", "rb")
    Contacts = pickle.load(pickle_off)

def see_contact():
    global Contacts
    unpic()
    print("Your Contact List")
    for person,info in Contacts.items():
        print(person, end=' ')
        for i in info :
            print(i,end=' || ')
        print("\n")

def new_contact():
    global Contacts
    unpic()
    print("Enter a new Contact")
    
    First_Name=input("First Name = ")
    Last_Name= input("Last Name = ")
    D_O_B=input("Date of Birth = ")
    Contact_No=input("Contact Number = ")
    email_id=input("Email ID = ")
    print("Thank You!!! Information recieved")

    Contacts.update({First_Name:[Last_Name,D_O_B,Contact_No,email_id]})
    pic()
    print("Saved New Contact!")

def edit_contact():
    global Contacts
    unpic()
    name=input("Enter First Name of the Contact to be edited : ")
    if name in Contacts.keys():
        
        x=Contacts.get(name)
        while True:
            print("\n 1. Enter to Edit First Name\n 2. Enter to edit last Name\n 3. Enter to edit  Dob\n 4. Enter to edit Phno Contact\n 5. Enter to edit emailid \n 6. Exit\n")
            choice=int(input()) 
            if choice==1:
                name_n = input("Enter New First Name : ")
                Contacts[name_n]= Contacts[name]
                del Contacts[name]
                print("First Name Changed")
            elif choice==2:
                last_name_n=input("Enter New Last Name : ")
                x[0]=last_name_n
                print("Last name changed")
            elif choice==3:
                d_o_b_n=input("Enter new Date of birth : ")
                x[1]=d_o_b_n
                print("Date of Birth changed")
            elif choice==4:
                cont_n=input("Enter new Contact No. : ")
                x[2]=cont_n
                print("Contact no changed")
            elif choice==5:
                email_n=input("Enter new email id : ")
                x[3]=email_n
                print("email id changed")
            elif choice==6:
                print("No further changes")
                break
    else :
        print("Contact Not Found")
    pic()

def search_contact():
    global Contacts
    unpic()
    name=input("Enter First Name of the Contact you want to search : ")
    if name in Contacts.keys():
        print(name,end=" ")
        x=Contacts.get(name)
        for i in x:
            print(i,end=" || ")
        
    else:
        print(f"{name} doesn't exit in your Contacts")
    pic()

def del_contact():
    global Contacts
    unpic()
    name=input("Enter First Name of the Contact yow want to delete : ")
    if name in Contacts.keys():
        Contacts.pop(name)
        print(f"{name} removed from your contact list")
    else:
        print(f"{name} doesn't exit in your Contacts")
    pic()

if __name__=="__main__":
    print("Welocome!!! This a Contact Book System")
    print("Enter a number to choose an action : ")
    
    while True:
        print("\n 1. See Contact List\n 2. Enter a new Contact\n 3. Edit an Existing Contact\n 4. Search a specific Contact\n 5. Delete a Contact\n 6. Exit\n")
        choice=int(input())
        if choice==1:
            see_contact()
        elif choice==2:
            new_contact()
        elif choice==3:
            edit_contact()
        elif choice==4:
            search_contact()
        elif choice==5:
            del_contact()
        elif choice==6:
            print("Thank you for using Contact Book System. Have a nice day!")
            exit()
        else:
            print("You entered an invalid number!!!")