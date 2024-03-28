import turtle
import random
import time
from time import sleep

# turtle
bob = turtle.Turtle()
bob.color("red")
bob.shapesize(2)
bob.shape("turtle")
# screen
game_screen = turtle.Screen()
game_screen.bgcolor("#66CDAA")
game_screen.title(" CATCH THE BOB")

count = 0  # counter
# header
turtle.penup()
turtle.teleport(0, 260)
turtle.hideturtle()


# counter method
def counter(x, y):
    global count
    count = count + 1
    print(count)


# timer set up
timer = turtle.Turtle()
start = time.time()
timer.teleport(0, 230)

for a in range(20):
    # turtle situated randomly
    bob.teleport(random.randint(-300, 300), random.randint(-300, 220))
    sleep(0.5)
    # timer
    timer.clear()
    timer.hideturtle()
    timer.write(19 - a, move=False, align="center", font=("Arial", 20, "normal"))
    # clicking
    turtle.listen()
    bob.onclick(fun=counter, btn=1, add=None)
# score board
turtle.write("your score : {}".format(count), move=False, align="center", font=("Arial", 30, "normal"))

turtle.mainloop()
