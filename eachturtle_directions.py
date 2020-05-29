import turtle

directions = ["directions-1.txt", "directions-2.txt", "directions-3.txt", "directions-4.txt", "directions-5.txt", "directions-6.txt"]
penColors = ["darkblue", "darkgreen", "darkred", "darkorange", "gold", "darkviolet"]
fillColors = ["blue", "lime", "red", "orange", "yellow", "violet"]
outputs = ["eachturtle-1.output", "eachturtle-2.output", "eachturtle-3.output", "eachturtle-4.output", "eachturtle-5.output", "eachturtle-6.output"]
fullpaths = ["(0,0)", "(0,0)", "(0,0)", "(0,0)", "(0,0)", "(0,0)"]
endpaths = ["", "", "", "", "", ""]
duppoints = ["", "", "", "", "", ""]

oneStep = 10.0

walks = []
files = []
for idx in range(len(directions)):
    files.append(open(directions[idx], 'r'))
    walks.append(files[idx].read())
    files[idx].close()

def moves(tortoise, walk, idx):
    for move in walk:
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

    endpaths[idx] = str(tuple(int(round((x / oneStep), 0)) for x in tortoise.position()))
    tortoise.write('End location ' + endpaths[idx])
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

    turtles[idx].pencolor(penColors[idx])
    turtles[idx].fillcolor(fillColors[idx])
    turtles[idx].shape("turtle")
    turtles[idx].setposition(0, 0)
    turtles[idx].setheading(90)
    turtles[idx].pendown()
    moves(turtles[idx], walks[idx], idx)

space.exitonclick()