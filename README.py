# CNA340_python99
import turtle ##import the turtle module
import random ##import the random module


wn = turtle.Screen()##create a screen

wn.bgcolor('lightblue')
wn.title("Turtle Race")##label the screen


lance = turtle.Turtle()##create two turtles

andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')
andyTotalDistance=0
lanceTotalDistance=0
andy.up()
lance.up()
andy.goto(andyTotalDistance, 20)
lance.goto(lanceTotalDistance, -20)

start = turtle.Turtle()  # OPTIONAL-##create a third turtle object called start that will be used to display the winner of the game

start.hideturtle()##hide the third turtle object until the game is over for aesthetic purposes


for i in range(150):##iterate through the loop to run the forward method on both turtles 150 times.

    ##make a random distance for andy to move
    andyDistance = random.randrange(1, 5)
    ##make a random distance for lance to move
    lanceDistance = random.randrange(1, 5)
    ##move andy forward and use the andyDistance variable to determine the amount to move forward by.
    andy.forward(andyDistance)
    ##move lance forward and use the lanceDistance variable to determine the amount to move forward by.
    lance.forward(lanceDistance)
    andyTotalDistance = andyTotalDistance + andyDistance
    lanceTotalDistance = lanceTotalDistance + lanceDistance
##De-indent to end the loop (use this twice)

for eachInt in range(145):
   ## use a cascading set of conditions to determine the winner.
    if andyTotalDistance > lanceTotalDistance:##Indent to begin the loop (use this twice)

        start.write("Andy is the winner!", move=False, align="center", font=("Arial", 25, "normal"))

    elif lanceTotalDistance > andyTotalDistance:##Indent to begin the loop (use this twice)

        start.write("Lance is the winner!", move=False, align="center", font=("Arial", 25, "normal"))
##De-indent to end the loop (use this twice)
    else: print("Tie Game")##this section is to determine the winner of the game and be used to print who the winner is.  It calculates total distance for lance and for andy.


wn.exitonclick()##exit on click of the window
