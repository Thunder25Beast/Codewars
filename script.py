import random
import math
from random import randint 
name = "script"

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
def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1


def moveAway(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1

def circleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
    # Get the current position of the pirate
    position = Pirate.getPosition()
    rx = position[0]  # x-coordinate of the pirate's current position
    ry = position[1]  # y-coordinate of the pirate's current position
    
    # Generate the positions around the center in a circular manner
    pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]  # Top arc
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])  # Right arc
    pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])  # Bottom arc
    pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])  # Left arc
    
    # Check if the pirate is not already on one of the positions
    if [rx, ry] not in pos:
        # If an initial position is specified and the pirate is not on one of the positions, move to the initial position
        if initial != "abc":
            return moveTo(initial[0], initial[1], Pirate)
        # If the pirate is within the circular path but not on one of the positions, move away from the center
        if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [y + i for i in range(-1 * radius, radius + 1)]:
            return moveAway(x, y, Pirate)
        # If the pirate is outside the circular path, move towards the center
        else:
            return moveTo(x, y, Pirate)
    else:
        # If the pirate is on one of the positions, determine the next position based on the clockwise direction
        index = pos.index([rx, ry])
        return moveTo(
            pos[(index + (clockwise * 2) - 1) % len(pos)][0],  # Calculate the x-coordinate of the next position
            pos[(index + (clockwise * 2) - 1) % len(pos)][1],  # Calculate the y-coordinate of the next position
            Pirate,
        )

def checkIsland(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    if (up[0:-1] == "island" or down[0:-1] == "island") and (left[0:-1] == "island" or right[0:-1] == "island"):
        return True
    else:
        return False

def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    
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
        return moveTo(x, y, pirate)
    else:

        return circleAround(20, 20, 19, pirate, initial="abc", clockwise=True)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()   
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")