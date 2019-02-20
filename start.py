#variable-----
light_switched = False

#functions------
def main():
    center()

def center ():
    print("You are in a nonagonal room. Each wall has")
    print("a door. They are numbered 1 through 9.")
    door= input("Select which number door you would like to go through")
    enter_from_center(door)

def enter_from_center(number):
    if number == "1":
        room_1()
    elif number == "2":
        room_2()
    elif number == "3":
        room_3(light_switched)
    elif number == "4":
        room_4(light_switched)
    elif number == "5":
        room_5()
    elif number == "6":
        room_6(light_switched)
    elif number == "7":
        room_7()
    elif number == "8":
        room_8(light_switched)
    elif number == "9":
        print("You pull the handle but the door is locked.")
        center()
    else:
        number= input("Select which number door you would like to go through") 
        enter_from_center(number)

def room_1():
    print("You are in a green room. You see a")
    print("small key sitting on a table.")
    command = input("Type exit to exit the room")
    exit_room(command)

def exit_room(command):
    if command == "exit":
        center()
    else: 
        command = input("Type exit to exit the room")
        exit_room(command)

def room_2():
    print("You are in a yellow room.")
    command = input("Type exit to exit the room")
    exit_room(command)    

def room_3(light_switched):
    print("You are in a room. It is pitch black.")
    command = input("Type exit to exit the room")
    exit_room(command)
    
def room_4(light_switched):
    print("You are in a room. It is pitch black.")
    command = input("Type exit to exit the room")
    exit_room(command) 
    
def room_5():
    print("You are in a pink room.")
    command = input("Type exit to exit the room")
    exit_room(command) 
    
def room_6(light_switched):
    print("You are in a blue room. You see a")
    print("light switch on the opposite wall.")
    command = input("Type exit to exit the room or light to pull the light switch")
    possible_answers= ["exit", "light"]
    while command not in possible_answers:
        command = input("Type exit to exit the room or light to pull the light switch")
    if command =="light":
        if light_switched == True:
            light_switched = False
        else:
            light_switched = True
        print(light_switched)
        room_6(light_switched)
    else:
        center() 
    
def room_7():
    print("You are in a white room.")
    command = input("Type exit to exit the room")
    exit_room(command)  

#this room gets dark when switch is flipped    
def room_8(light_switched):
    print("You are in an orange room. There is a door on the north wall.")
    command = input("Type exit to exit the room or north to go through the door")
    possible_answers= ["exit", "north"]
    while command not in possible_answers:
        command = input("Type exit to exit the room or north to go through the door")
    if command =="north":
        room_9()
    else:
        center()
    
def room_9():
    print("You are in a red room. There is a door on the south wall.")
    command = input("Type exit to exit the room or south to go through the door")
    possible_answers= ["exit", "south"]
    while command not in possible_answers:
        command = input("Type exit to exit the room or south to go through the door")
    if command =="south":
        room_8()
    else:
        center()

#run--------------    
if __name__ == "__main__":
    main()
