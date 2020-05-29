import turtle

directions = ["directions-1.txt", "directions-2.txt", "directions-3.txt", "directions-4.txt", "directions-5.txt", "directions-6.txt"]
penColors = ["darkblue", "darkgreen", "darkred", "darkorange", "gold", "darkviolet"]
fillColors = ["blue", "lime", "red", "orange", "yellow", "violet"]
outputs = ["allturtle-1.output", "allturtle-2.output", "allturtle-3.output", "allturtle-4.output", "allturtle-5.output", "allturtle-6.output"]
fullpaths = ["(0,0)", "(0,0)", "(0,0)", "(0,0)", "(0,0)", "(0,0)"]
endpaths = ["", "", "", "", "", ""]
duppoints = ["", "", "", "", "", ""]

oneStep = 10

walks = []
files = []

for idx in range(len(directions)):
    files.append(open(directions[idx], 'r'))
    walks.append(files[idx].read())
    files[idx].close()

maxWalkLen = 0
for idx in range(len(directions)):
    if maxWalkLen < len(walks[idx]):
        maxWalkLen = len(walks[idx])

def oneMove(tortoise, move, idx):
        if move == 'L':
            tortoise.left(90)
        elif move == 'R':
            tortoise.right(90)
        elif move == 'F':
            tortoise.forward(oneStep)
            posStr = str(tuple(int(round((x / oneStep), 0)) for x in tortoise.position()))
            if posStr in fullpaths[idx]:
                if posStr not in duppoints[idx]:
                    tortoise.dot(fillColors[idx])
                    tortoise.write(posStr)
                    if duppoints[idx] == "":
                        duppoints[idx] += posStr
                    else:
                        duppoints[idx] += ", " + posStr
            fullpaths[idx] += ", " + posStr

def moves(walks):
  for stepNo in range(maxWalkLen):
    for idx in range(len(directions)):
        if stepNo < len(walks[idx]):
            oneMove(turtles[idx], walks[idx][stepNo], idx)
        if stepNo == (len(walks[idx])-1):
            endpaths[idx] = str(tuple(int(round((x / oneStep), 0)) for x in turtles[idx].position()))
            turtles[idx].write('End location ' + endpaths[idx])
            print(directions[idx])
            print('----------------------------------------------')
            print('End location: ' + endpaths[idx])
            print('Full Path: ' + fullpaths[idx])
            print('Points visited more than once: ' + duppoints[idx])
            print('----------------------------------------------')
            print('\n\n')

            files[idx] = open(outputs[idx], 'w+')
            files[idx].write(directions[idx] + '\n')
            files[idx].write('----------------------------------------------\n')
            files[idx].write('End location: ' + endpaths[idx] + '\n')
            files[idx].write('Full Path: ' + fullpaths[idx] + '\n')
            files[idx].write('Points visited more than once: ' + duppoints[idx] + '\n')
            files[idx].write('----------------------------------------------')
            files[idx].close()

space = turtle.Screen()

turtles = []
for idx in range(len(directions)):
    turtles.append(turtle.Turtle())

for idx in range(len(directions)):
    turtles[idx].pencolor(penColors[idx])
    turtles[idx].fillcolor(fillColors[idx])
    turtles[idx].shape("turtle")
    turtles[idx].setposition(0, 0)
    turtles[idx].setheading(90)
    turtles[idx].pendown()

moves(walks)

space.exitonclick()