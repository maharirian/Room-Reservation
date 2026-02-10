all_room_list = {"room1":"big","room2":"big","room3":"small","room4":"small"}
empty_room_list = []
reserve_list = {"room1":"ali"}
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

def show_empty_rooms():
    for room in all_room_list:
        if room not in reserve_list:
            empty_room_list.append(room)
    if empty_room_list:
        print("Empty rooms:", ", ".join(empty_room_list))
    else:
        print("No empty rooms available.")

def show_reserve_rooms():
    if reserve_list:
        print("Reserved rooms:")
        for room, person in reserve_list.items():
            print(f"{room} --> reserved by {person}")
    else:
        print("No rooms are reserved.")


while True:
    print("=== Login ===")
    name = input("Enter name: ").strip()
    pas = input("Enter password: ").strip()
    
    if admin_list.get(name) == pas:
        print("Login successfully as admin!")
        while True:
            print("\nAdmin Menu:\n 1. Add new member\n 2. Delete member\n 3. Show empty room\n 4. Show reserv room \n 8. Logout")
            choice = input("Enter your choice: ").strip()
            options = {
                '1': add_member,
                '2': del_member,
                '3': show_empty_rooms,
                '4': show_reserve_rooms,
            }
            if choice == '8':
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

