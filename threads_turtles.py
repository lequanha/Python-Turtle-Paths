import queue
import threading
import turtle

directions = ["directions-1.txt", "directions-2.txt", "directions-3.txt", "directions-4.txt", "directions-5.txt", "directions-6.txt"]
penColors = ["darkblue", "darkgreen", "darkred", "darkorange", "gold", "darkviolet"]
fillColors = ["blue", "lime", "red", "orange", "yellow", "violet"]

oneStep = 10

walks = []
files = []
for idx in range(len(directions)):
    files.append(open(directions[idx], 'r'))
    walks.append(files[idx].read())
    files[idx].close()

def moves(tortoise, walk):
    for move in walk:
        if move == 'L':
            graphics.put((tortoise.left, 90))
        elif move == 'R':
            graphics.put((tortoise.right, 90))
        elif move == 'F':
            graphics.put((tortoise.forward, oneStep))

def process_queue():
    while not graphics.empty():
        graphic, argument = graphics.get()
        graphic(argument)


space = turtle.Screen()
graphics = queue.Queue(1)  # size = number of hardware threads you have - 1

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

threads = []
for idx in range(len(directions)):
    threads.append(threading.Thread(target=moves, args=(turtles[idx], walks[idx])))

for idx in range(len(directions)):
    threads[idx].daemon = True  # thread dies when main thread (only non-daemon thread) exits.
    threads[idx].start()

process_queue()

space.exitonclick()