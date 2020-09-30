# import sys
from shutil import move

def name_robot():
    return input("What do you want to name your robot? ")

def robot_start():
    """This is the entry function, do not change"""
    name = name_robot()
    print(f"{name}: Hello kiddo!")
    check_command(name)

def help_command():
    print("I can understand these commands:")
    print("OFF  - Shut down robot")
    print("HELP - provide information about commands\n")  

def move_forward(x,y,find,name,split,degrees):
    step = int(split[1])
    if degrees == 0:
        y += step
    if degrees == 90:
        x += step
    if degrees == 180:
        y -= step
    if degrees == 270:
        x -= step
    if (y < -200 or y > 200)  or (x < -100 or x > 100):
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        return reverse_move(x,y,find,name,split,degrees)        
    return (x,y,find)
    

def move_back(x,y,find,name,split,degrees):
    step = int(split[1])
    if degrees == 0:
        y -= step
    if degrees == 90:
        x -= step
    if degrees == 180:
        y += step
    if degrees == 270:
        x += step 
    if (y < -200 or y > 200)  or (x < -100 or x > 100):
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        return reverse_move(x,y,find,name,split,degrees)
    return (x,y,find)

def move_sprint(x,y,name,split,degrees):
    step = int(split[1])
    while step > 0:
        if degrees == 0:
            y += step
        if degrees == 90:
            x += step
        if degrees == 180:
            y -= step
        if degrees == 270:
            x -= step
        print(f" > {name} moved forward by {step} steps.")
        step -= 1
        split[1] = str(step)
        return move_sprint(x,y,name,split,degrees)
    return(x,y)        


def reverse_move(x,y,find,name,split,degrees):
    find = 1
    if split[0] == 'back':
        return move_forward(x,y,find,name,split,degrees)
    elif split[0] == 'forward':
        return move_back(x,y,find,name,split,degrees)


def turn_axis(name,degrees,split):
    if split[0] == 'right':
        degrees += 90 
    if split[0] == 'left':  
        degrees -= 90
    if degrees == 360:
        degrees = 0
    if degrees < 0:
        degrees = 270    
    print(f" > {name} turned {split[0]}.")
    return degrees         

def check_command(name):
    commands = ['off','help','right','left','sprint','forward','back']
    coordinates = [0, 0]
    degrees = 0
    x = coordinates[0]
    y = coordinates[1]
    while True:
        find = 0
        split_cmd = get_command_input(name,commands)

        if commands[0] == split_cmd[0].lower():
            print(f"{name}: Shutting down..")
            break
        elif commands[1] == split_cmd[0].lower():
            help_command()
            continue
        elif commands[2] == split_cmd[0].lower():
            degrees = turn_axis(name,degrees,split_cmd)       
        elif commands[3] == split_cmd[0].lower():            
            degrees = turn_axis(name,degrees,split_cmd)
        elif commands[4]  == split_cmd[0].lower():
            x,y = move_sprint(x,y,name,split_cmd,degrees)    
        else:                
            if commands[5] == split_cmd[0].lower():            
                x,y,find = move_forward(x,y,find,name,split_cmd,degrees)
                # print(find)
                if find ==  0:
                    print(f" > {name} moved {split_cmd[0].lower()} by {split_cmd[1]} steps.")
            elif commands[6] == split_cmd[0].lower():            
                x,y,find = move_back(x,y,find,name,split_cmd,degrees)
                if find == 0:
                    print(f" > {name} moved {split_cmd[0].lower()} by {split_cmd[1]} steps.")
        print(f" > {name} now at position ({x},{y}).")            

def get_command_input(name,commands):
    while True:
        cmd = input(f"{name}: What must I do next? ")
        split_cmd = cmd.split(' ')
        if len(split_cmd) == 1 and split_cmd[0].lower() in commands[:4]:
            return split_cmd
        elif (len(split_cmd) == 2) and (split_cmd[0].lower() in commands[4:]):
            if split_cmd[1].isdigit():
                return split_cmd
        else:
            print(f"{name}: Sorry, I did not understand '{cmd}'.")

            
if __name__ == "__main__":
    robot_start()













