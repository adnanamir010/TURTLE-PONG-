import turtle

#Defining the screen elements
#Blue screen
screen = turtle.Screen()
screen.title("Pong by Adnan")
screen.bgcolor("green")
screen.setup(width=1000, height=600)

#Player 1 paddle
playerone_pad = turtle.Turtle()
playerone_pad.speed(0)
playerone_pad.shape("square")
playerone_pad.color("black")
playerone_pad.shapesize(stretch_wid=6, stretch_len=2)
playerone_pad.penup()
playerone_pad.goto(-400, 0)

#Player 2 paddle
playertwo_pad = turtle.Turtle()
playertwo_pad.speed(0)
playertwo_pad.shape("square")
playertwo_pad.color("black")
playertwo_pad.shapesize(stretch_wid=6, stretch_len=2)
playertwo_pad.penup()
playertwo_pad.goto(400, 0)

#ball
pong = turtle.Turtle()
pong.speed(1000)
pong.shape("circle")
pong.color("yellow")
pong.penup()
pong.goto(0, 0)
pong.dx = 5
pong.dy = -5

#Scoreboard
playeroneScore = 0
playertwoScore = 0
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0	Player 2: 0", align="center", font=("Courier", 24, "normal"))

#______________________________________________________________________________________________________________________________________________________
#Defining Controls
#Up and Down for Player 1 and Player 2 paddle
def oneUp():
	y = playerone_pad.ycor()
	y += 20
	playerone_pad.sety(y)


def oneDown():
	y = playerone_pad.ycor()
	y -= 20
	playerone_pad.sety(y)


def twoUp():
	y = playertwo_pad.ycor()
	y += 20
	playertwo_pad.sety(y)


def twoDown():
	y = playertwo_pad.ycor()
	y -= 20
	playertwo_pad.sety(y)

#Keybindings
screen.listen()
screen.onkeypress(oneUp, "w")
screen.onkeypress(oneDown, "s")
screen.onkeypress(twoUp, "Up")
screen.onkeypress(twoDown, "Down")
#______________________________________________________________________________________________________________________________________________________
#Game Design
#initializing loop
while True:
	screen.update()
#setting direction of ball
	pong.setx(pong.xcor()+pong.dx)
	pong.sety(pong.ycor()+pong.dy)

#Collisions with walls on top and bottom
#Top
	if pong.ycor() > 280:
		pong.sety(280)
		pong.dy *= -1
#bottom
	if pong.ycor() < -280:
		pong.sety(-280)
		pong.dy *= -1

#Scoring if ball makes it through left or right side
#Ball passes through Right Side
	if pong.xcor() > 500:
		pong.goto(0, 0)
		pong.dy *= -1
		playeroneScore += 1
		score.clear()
		score.write("Player 1: {}	Player 2: {}".format(playeroneScore, playertwoScore), align="center",font=("Courier", 24, "normal"))
#Ball passes through Left Side
	if pong.xcor() < -500:
		pong.goto(0, 0)
		pong.dy *= -1
		playertwoScore += 1
		score.clear()
		score.write("Player 1: {}	Player 2: {}".format(playeroneScore, playertwoScore), align="center",font=("Courier", 24, "normal"))
		#______________________________________________________________________________________________________________________________________________________
#Collisions
#If ball hits left side paddle (player 1 paddle)
	if (pong.xcor()<-360 and pong.xcor()>-370) and (pong.ycor()<playerone_pad.ycor()+40 and pong.ycor()>playerone_pad.ycor()-40):
		pong.setx(-360)
		pong.dx*=-1
#If ball hits right side paddle (player 2 paddle)
	if (pong.xcor() > 360 and pong.xcor() < 370) and (pong.ycor() < playertwo_pad.ycor()+40 and pong.ycor() > playertwo_pad.ycor()-40):
		pong.setx(360)
		pong.dx*=-1
