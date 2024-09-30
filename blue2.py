import random 
from random import randint
name = 'sample2'
import math
def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
    
def checkfriends(pirate , quad ):
    sum = 0 
    up = pirate.investigate_up()[1]
    print(up)
    down = pirate.investigate_down()[1]
    left = pirate.investigate_left()[1]
    right = pirate.investigate_right()[1]
    ne = pirate.investigate_ne()[1]
    nw = pirate.investigate_nw()[1]
    se = pirate.investigate_se()[1]
    sw = pirate.investigate_sw()[1]
    
    if(quad=='ne'):
        if(up == 'friend'):
            sum +=1 
        if(ne== 'friend'):
            sum +=1 
        if(right == 'friend'):
            sum +=1 
    if(quad=='se'):
        if(down == 'friend'):
            sum +=1 
        if(right== 'friend'):
            sum +=1 
        if(se == 'friend'):
            sum +=1 
    if(quad=='sw'):
        if(down == 'friend'):
            sum +=1 
        if(sw== 'friend'): 
            sum +=1 
        if(left == 'friend'):
            sum +=1 
    if(quad=='nw'):
        if(up == 'friend'):
            sum +=1 
        if(nw == 'friend'):
            sum +=1 
        if(left == 'friend'):
            sum +=1 

    return sum

import random

def spread(pirate):
    # Define the coordinates of the center of the map
    map_center_x = pirate.getDimensionX() // 2
    map_center_y = pirate.getDimensionY() // 2
    
    # Get the current position of the pirate
    current_x, current_y = pirate.getPosition()
    
    # Determine the direction to move based on the relative position to the center
    if current_x < map_center_x and current_y < map_center_y:
        # If the pirate is in the top-left quadrant, move towards the bottom-right
        return moveTo(map_center_x + 5, map_center_y + 5, pirate)
    elif current_x < map_center_x and current_y > map_center_y:
        # If the pirate is in the bottom-left quadrant, move towards the top-right
        return moveTo(map_center_x + 5, map_center_y - 5, pirate)
    elif current_x > map_center_x and current_y < map_center_y:
        # If the pirate is in the top-right quadrant, move towards the bottom-left
        return moveTo(map_center_x - 5, map_center_y + 5, pirate)
    elif current_x > map_center_x and current_y > map_center_y:
        # If the pirate is in the bottom-right quadrant, move towards the top-left
        return moveTo(map_center_x - 5, map_center_y - 5, pirate)
    else:
        # If the pirate is at the center or along the edges, move randomly
        return random.randint(1, 4)

#def spread(pirate):
    sw = checkfriends(pirate ,'sw' )
    se = checkfriends(pirate ,'se' )
    ne = checkfriends(pirate ,'ne' )
    nw = checkfriends(pirate ,'nw' )
   
    my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    x, y = pirate.getPosition()
    
    if( x == 0 and y == 0):
        return randint(1,4)
    
    if(sorted_dict[list(sorted_dict.keys())[3]] == 0 ):
        return randint(1,4)
    
    if(list(sorted_dict())[0] == 'sw'):
        return moveTo(x-1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'se'):
        return moveTo(x+1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'ne'):
        return moveTo(x+1 , y-1 , pirate)
    elif(list(sorted_dict())[0] == 'nw'):
        return moveTo(x-1 , y-1 , pirate)

def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    
    
    if (
    ((up == "island1" and s[0] == "myCaptured") +
     (up == "island2" and s[1] == "myCaptured") +
     (up == "island3" and s[2] == "myCaptured")) == 1 or
     ((down == "island1" and s[0] == "myCaptured") +
     (down == "island2" and s[1] == "myCaptured") +
     (down == "island3" and s[2] == "myCaptured")) == 1 or
     ((right == "island1" and s[0] == "myCaptured") +
     (right == "island2" and s[1] == "myCaptured") +
     (right == "island3" and s[2] == "myCaptured")) == 1 or
     ((left == "island1" and s[0] == "myCaptured") +
     (left == "island2" and s[1] == "myCaptured") +
     (left == "island3" and s[2] == "myCaptured")) == 1
    ):
       # s = up[-1] + str(x) + "," + str(y - 1)
       # pirate.setTeamSignal(s)
        spread(pirate)

    else:

            if (
                (up == "island1" and s[0] != "myCaptured")
                or (up == "island2" and s[1] != "myCaptured")
                or (up == "island3" and s[2] != "myCaptured")
            ):
                s = up[-1] + str(x) + "," + str(y - 1)
                pirate.setTeamSignal(s)

            if (
                (down == "island1" and s[0] != "myCaptured")
                or (down == "island2" and s[1] != "myCaptured")
                or (down == "island3" and s[2] != "myCaptured")
            ):
                s = down[-1] + str(x) + "," + str(y + 1)
                pirate.setTeamSignal(s)

            if (
                (left == "island1" and s[0] != "myCaptured")
                or (left == "island2" and s[1] != "myCaptured")
                or (left == "island3" and s[2] != "myCaptured")
            ):
                s = left[-1] + str(x - 1) + "," + str(y)
                pirate.setTeamSignal(s)

            if (
                (right == "island1" and s[0] != "myCaptured")
                or (right == "island2" and s[1] != "myCaptured")
                or (right == "island3" and s[2] != "myCaptured")
            ):
                s = right[-1] + str(x + 1) + "," + str(y)
                pirate.setTeamSignal(s)


            if pirate.getTeamSignal() != "":
                s = pirate.getTeamSignal()
                l = s.split(",")
                x = int(l[0][1:])
                y = int(l[1])

                if (int(pirate.getID() )% 5) != 0 :
                    return moveTo(x,y,pirate)
                else :
                    if(left == "island1" or left == "island2"  or left == "island3" 
                    ):
                        return 4
                    if(right == "island1" or right == "island2"  or right == "island3" 
                    ):
                        return 2
                    if(up == "island1" or up == "island2"  or up == "island3" 
                    ):
                        return 1
                    if(down == "island1" or down == "island2"  or down == "island3" 
                    ):
                        return 3

                    else:
                        return random.randint(1,4)

            else:
                return random.randint(1,4)
            
def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
   
    if s:
        print(s)
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")