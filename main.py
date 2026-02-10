room_list = {"room1":"big","room2":"big","room3":"small","room4":"small"}
reserv_list = []
admin_list = {"admin":"abcd"}
user_list = {}

def add_member():
    key = input("add user or admin:")
    if key =="admin":
        name = input("enter name:") 
        pas = input("enter pasword:")
        admin_list[name] = pas
        print("admin successfully added")
    elif key =="user":
        name = input("enter name:") 
        pas = input("enter pasword:")
        user_list[name] = pas
        print("user successfully added")
    else:
        print("error to add member")


while True:
    print("login")
    name = input("enter name:") 
    pas = input("enter pasword:")      
    if admin_list.get(name) == pas:
        print("login successfully")
        print("menu \n 1.add new user \n 2.add new admin")
    elif user_list.get(name) == pas:
        print("login successfully")
        print("menu \n 1.show room \n 2.my reserv")
