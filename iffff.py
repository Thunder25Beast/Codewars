(
    ((up == "island1" and s[0] == "myCaptured") +
     (up == "island2" and s[1] == "myCaptured") +
     (up == "island3" and s[2] == "myCaptured")) == 1
    ):

        s = up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

        if pirate.getTeamSignal() != "":
            s = pirate.getTeamSignal()
            l = s.split(",")
            x = int(l[0][1:])
            y = int(l[1])
            x1= pirate.getDimensionX()/2
            r=math.sqrt( (x-x1)**2+(y-x1)**2 ) 
            (x3, y3) = round(x1+r*(-0.5) + (x - x1) * (-0.5) - (y - x1) * 0.866),round( x1 + r * 0.866 + (x - x1) * 0.866 + (y - x1) * (-0.5))
            (x2, y2) = round(x1 + r * (-0.5) + (x - x1) * (-0.5) - (y - x1) * (-0.866)),round( x1 + r * (-0.866) + (x - x1) * (-0.866) + (y - x1) * (-0.5))
            print(x2,y2)
            print(x3,y3)
            if(int(pirate.getID())%2==0):
                return moveTo(x2+randint(-5,5),y2+randint(-5,5),pirate)
            else:
                return moveTo(x3+randint(-5,5),y3+randint(-5,5),pirate)
        else:return random.randint(1,4)
    if ( 
     (down == "island1" and s[0] == "myCaptured") +
     (down == "island2" and s[1] == "myCaptured")+
     (down == "island3" and s[2] == "myCaptured")==1
    ):
        s = down[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

        if pirate.getTeamSignal() != "":
            s = pirate.getTeamSignal()
            l = s.split(",")
            x = int(l[0][1:])
            y = int(l[1])
            x1= pirate.getDimensionX()/2
            r=math.sqrt( (x-x1)**2+(y-x1)**2 ) 
            (x3, y3) = round(x1+r*(-0.5) + (x - x1) * (-0.5) - (y - x1) * 0.866),round( x1 + r * 0.866 + (x - x1) * 0.866 + (y - x1) * (-0.5))
            (x2, y2) = round(x1 + r * (-0.5) + (x - x1) * (-0.5) - (y - x1) * (-0.866)),round( x1 + r * (-0.866) + (x - x1) * (-0.866) + (y - x1) * (-0.5))
            print(x2,y2)
            print(x3,y3)
            if(int(pirate.getID())%2==0):
                return moveTo(x2+randint(-5,5),y2+randint(-5,5),pirate)
            else:
                return moveTo(x3+randint(-5,5),y3+randint(-5,5),pirate)
        else:return random.randint(1,4)
    if (
     (left == "island1" and s[0] == "myCaptured") +
     (left == "island2" and s[1] == "myCaptured")+
     (left == "island3" and s[2] == "myCaptured")==1
    ):
        s = left[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

        if pirate.getTeamSignal() != "":
            s = pirate.getTeamSignal()
            l = s.split(",")
            x = int(l[0][1:])
            y = int(l[1])
            x1= pirate.getDimensionX()/2
            r=math.sqrt( (x-x1)**2+(y-x1)**2 ) 
            (x3, y3) = round(x1+r*(-0.5) + (x - x1) * (-0.5) - (y - x1) * 0.866),round( x1 + r * 0.866 + (x - x1) * 0.866 + (y - x1) * (-0.5))
            (x2, y2) = round(x1 + r * (-0.5) + (x - x1) * (-0.5) - (y - x1) * (-0.866)),round( x1 + r * (-0.866) + (x - x1) * (-0.866) + (y - x1) * (-0.5))
            print(x2,y2)
            print(x3,y3)
            if(int(pirate.getID())%2==0):
                return moveTo(x2+randint(-5,5),y2+randint(-5,5),pirate)
            else:
                return moveTo(x3+randint(-5,5),y3+randint(-5,5),pirate)
        else:return random.randint(1,4)
    if (

     (right == "island1" and s[0] == "myCaptured")+
     (right == "island2" and s[1] == "myCaptured")+
     (right == "island3" and s[2] == "myCaptured")==1
    ):
        s = right[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

        if pirate.getTeamSignal() != "":
            s = pirate.getTeamSignal()
            l = s.split(",")
            x = int(l[0][1:])
            y = int(l[1])
            x1= pirate.getDimensionX()/2
            r=math.sqrt( (x-x1)**2+(y-x1)**2 ) 
            (x3, y3) = round(x1+r*(-0.5) + (x - x1) * (-0.5) - (y - x1) * 0.866),round( x1 + r * 0.866 + (x - x1) * 0.866 + (y - x1) * (-0.5))
            (x2, y2) = round(x1 + r * (-0.5) + (x - x1) * (-0.5) - (y - x1) * (-0.866)),round( x1 + r * (-0.866) + (x - x1) * (-0.866) + (y - x1) * (-0.5))
            print(x2,y2)
            print(x3,y3)
            if(int(pirate.getID())%2==0):
                return moveTo(x2+randint(-5,5),y2+randint(-5,5),pirate)
            else:
                return moveTo(x3+randint(-5,5),y3+randint(-5,5),pirate)
        else:return random.randint(1,4)
        