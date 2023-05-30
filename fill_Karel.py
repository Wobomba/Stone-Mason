from stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():

    sparrow()
#after reaching the end place a beeper and turn west
def turn_around():
    put_beeper()
    turn_left()
    turn_left()
    
#putting all methods together
def sparrow():
    #while facing east
    while front_is_clear():
        put_beeper()
        move()
    turn_around() #turning to face west
    back_to_start()#heading to the start point
    to_face_north() #facing north
    to_face_east() #turning from north to east
    
    #checking if beepers are present else recursively calling the function
    if beepers_present():
        turn_left()
        pass
    else:
        sparrow()

def back_to_start():
    while front_is_clear():
        move()

def to_face_north():
    turns()
    
    #checking if north is clear
    if front_is_clear():
        move()
    
    else: #else if the north is blocked then don't move there
        turns()
        while front_is_clear():
            move()
            pass
 
def to_face_east():
    turns()
    
#3turns
def turns():
    for i in range(3):
        turn_left()
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
   run_karel_program()