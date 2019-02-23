#variables-----
light_switched = False
has_small_key = False
has_large_key = False
entered_room = [True, False, False, False, False, False, False, False, False, False]

#functions------
def main():
    center()

def center ():
    print("You are in a nonagonal room. Each wall has")
    print("a door. They are numbered 1 through 9.")
    if False in entered_room:
        door= input("Select which number door you would like to go through")
        enter_from_center(door)
    else:
        print("A tenth wall appears with a door. You exit through the door, winning the game.")

def enter_from_center(number):
    if number == "1":
        room_1()
    elif number == "2":
        room_2()
    elif number == "3":
        room_3()
    elif number == "4":
        room_4()
    elif number == "5":
        room_5()
    elif number == "6":
        room_6()
    elif number == "7":
        room_7()
    elif number == "8":
        room_8()
    elif number == "9":
        print("You pull the handle but the door is locked.")
        center()
    else:
        number= input("Select which number door you would like to go through") 
        enter_from_center(number)

def room_1():
    global has_small_key
    print("You are in a green room.")
    entered_room[1] = True 
    if has_small_key == False:
        print("You see a small key sitting on a table.") 
        command = input("Type exit to exit the room or key to pick up the key")
        possible_answers= ["exit", "key"]
        while command not in possible_answers:
            command = input("Type exit to exit the room or key to pick up the key")
        if command == "exit":
            center()
        else:
            print("You have picked up the key.")
            has_small_key = True
            room_1()
    else:
        command = input("Type exit to exit the room")
        exit_room(command) 

def exit_room(command):
    if command == "exit":
        center()
    else: 
        command = input("Type exit to exit the room")
        exit_room(command)

def room_2():
    global has_large_key
    if has_large_key == True:
        entered_room[2] = True
        print("You have unlocked the door. You are in a yellow room.")#locked
        command = input("Type exit to exit the room")
        exit_room(command)  
    else:
        print("The door is locked. You need a large key to enter.")  
        center()

def room_3():
    global light_switched
    entered_room[3] = True
    if light_switched == True:
        print("You are in a brown room.")
    else:
        print("You are in a room. It is pitch black.")
    command = input("Type exit to exit the room")
    exit_room(command)
    
def room_4():
    global light_switched
    entered_room[4] = True
    if light_switched == True:
        print("You are in a purple room.")
    else:
        print("You are in a room. It is pitch black.")
    command = input("Type exit to exit the room")
    exit_room(command) 
    
def room_5():
    entered_room[5] = True
    print("You are in a pink room.")
    command = input("Type exit to exit the room")
    exit_room(command) 
    
def room_6():
    global light_switched
    entered_room[6] = True
    print("You are in a blue room. You see a")
    print("light switch on the opposite wall.")
    command = input("Type exit to exit the room or light to pull the light switch")
    possible_answers= ["exit", "light"]
    while command not in possible_answers:
        command = input("Type exit to exit the room or light to pull the light switch")
    if command =="light":
        print("You have flipped the light switch.")
        if light_switched == True:
            light_switched = False
        else:
            light_switched = True
        room_6()
    else:
        center() 
    
def room_7(): #has a locked box with another key to rm 2
    global has_small_key
    global has_large_key
    entered_room[7] = True
    print("You are in a white room.")
    print("There is a box on a table.")
    command = input("Type exit to exit the room or box to unlock the box")
    possible_answers= ["exit", "box"]
    while command not in possible_answers:
        command = input("Type exit to exit the room or box to unlock the box")
    if command == "box":
        if has_small_key == True:
            if has_large_key == False:
                print("You have unlocked the box. Inside you find a large key.")
                command = input("Type exit to leave the box or key to pick up the key")
                possible_answers= ["exit", "key"]
                while command not in possible_answers:
                    command = input("Type exit to leave the box or key to pick up the key")
                if command == "exit":
                    room_7()   
                else:
                    print("You have picked up the large key")
                    has_large_key = True 
                    room_7()
            else: 
                print("You have unlocked the box. Inside it is empty.")
                command = input("Type exit to leave the box")
                possible_answers= ["exit"]
                while command not in possible_answers:
                    command = input("Type exit to leave the box")
                if command == "exit":
                    room_7()
        else:
            print("The box is locked. You need a key to open it.")
            room_7()
    else: 
        center()  

#this room gets dark when switch is flipped    
def room_8():
    global light_switched
    entered_room[8] = True
    if light_switched == True:
        print("You are in a room. It is pitch black.")
        command = input("Type exit to exit the room")
        exit_room(command)
    else:
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
    entered_room[9] = True
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
