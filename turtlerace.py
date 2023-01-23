from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(500,400)
is_game_on=False
choice=screen.textinput(title="Enter your bet",prompt="Which turtle will win the race ?")
color=["red","green","yellow","orange","blue","green"]
all_turtles=[]
for i in range(6):
   new_turtle=Turtle(shape="turtle")
   new_turtle.color(color[i])
   new_turtle.penup()
   new_turtle.goto(-240, -100 + 30 * i)
   all_turtles.append(new_turtle)
if choice:
    is_game_on=True

while is_game_on:
    for turtle in all_turtles:
        if(turtle.xcor()>230):
            is_game_on=False
            winningturtle=turtle.pencolor()
            if(choice==winningturtle):
                print(f"You have won.The winning turtle is {winningturtle}.")
            else:
                print(f"You have loss.The winning turtle is {winningturtle}.")
        r=random.randint(0,10)
        turtle.forward(r)

screen.exitonclick()