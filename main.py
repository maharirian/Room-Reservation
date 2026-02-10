room_list = {"room1":"big","room2":"big","room3":"small","room4":"small"}
reserv_list = []
admin_list = {"admin":"a"}
user_list = {"ali":"ab"}



#admin func
def add_member():
    key = input("add user or admin:")
    if key =="admin":
        name = input("enter name:") 
        pas = input("enter pasword:")
        admin_list[name] = pas
        print("admin successfully added")
        print(admin_list)
    elif key =="user":
        name = input("enter name:") 
        pas = input("enter pasword:")
        user_list[name] = pas
        print("user successfully added")
        print(user_list)
    else:
        print("error to add member")

def del_member():
    key = input("del user or admin:")
    if key =="admin":
        name = input("enter name:") 
        del admin_list[name]
        print("admin successfully deleted")
        print(admin_list)
    elif key =="user":
        name = input("enter name:") 
        del user_list[name]
        print("user successfully deleted")
        print(user_list)
    else:
        print("error to delete member")

while True:
    print("=== Login ===")
    name = input("Enter name: ").strip()
    pas = input("Enter password: ").strip()
    
    if admin_list.get(name) == pas:
        print("Login successfully as admin!")
        while True:
            print("\nAdmin Menu:\n 1. Add new member\n 2. Delete member\n 3. Logout")
            choice = input("Enter your choice: ").strip()
            options = {
                '1': add_member,
                '2': del_member,
            }
            if choice == '3':
                print("Logging out...")
                break
            action = options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice, please try again")
    
    elif user_list.get(name) == pas:
        print("Login successfully as user!")
        
    else:
        print("Invalid username or password. Try again.")

