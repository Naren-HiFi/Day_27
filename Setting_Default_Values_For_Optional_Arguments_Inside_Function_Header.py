'''
Advanced Python Arguments
'''

from turtle import Turtle, Screen

gui_screen = Screen()
gui_screen.title("Ninja Turtle")
gui_screen.setup(width=500, height=300)
ninja = Turtle()
ninja.shape("turtle")
ninja.color("black")
ninja.write("Some text", font=("Times New Roman", 30, 'bold'))

gui_screen.exitonclick()

def foo(a,b=4, c=6):
    print(a,b,c)

foo(1)

def coo(a,b=4, c=6):
    print(a,b,c)

coo(4,9)