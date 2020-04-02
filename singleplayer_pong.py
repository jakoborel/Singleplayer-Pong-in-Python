'''
This version writes every score to the file to find the average score, 
low score, and high score. This is inefficient and causes problems when a large
number of games is played.
'''
from turtle import Turtle, Screen
from random import choice, randint
import time

#opens a file if not already made to store scores
f = open("scores.txt", "a+")
averageScore = 0
highScore = 0
lowScore = 0

#initialize score variables if file has previous scores
for line in f:
    scoresInLine = line.split()
    scoresInLine = [int(x) for x in scoresInLine]
    averageScore = (sum(scoresInLine))//(len(scoresInLine))
    highScore = max(scoresInLine)
    lowScore = min(scoresInLine)
    
#modifiable starting variables
courtWidth = 800
courtHeight = 600

playerHeight = 20
playerWidth = 80
turtleFactor = 20 #factor by which turtlesize scaling is off

FONT = ("device", 25, "normal")
FONT2 = ("device", 12, "bold")
FONT3 = ("device", 15, "bold")

ballSpeed = 6
playerSpeed = 49

#Initialize score, highscore, lowscore, and average scores and turtles
score = 0
s = Turtle(visible=False)
s.speed("fastest")
s.color("white")
s.penup()
s.setposition(-courtWidth/2, courtHeight-300)
s.write("Score: " + str(score), font = FONT)

hs = Turtle(visible=False)
hs.speed("fastest")
hs.color("#28aa05")
hs.penup()
hs.setposition(-courtWidth + 550, courtHeight-300)
hs.write("Highscore: " + str(highScore), font = FONT)

ls = Turtle(visible=False)
ls.speed("fastest")
ls.color("#ba1e0d")
ls.penup()
ls.setposition(-courtWidth + 760, courtHeight-300)
ls.write("Lowscore: " + str(lowScore), font = FONT)

avs = Turtle(visible=False)
avs.speed("fastest")
avs.color("#912bc6")
avs.penup()
avs.setposition(courtWidth/2 - 250, courtHeight-300)
avs.write("Average Score: " + str(averageScore), font = FONT)

#initializes pause turtle
ps = Turtle(visible=False)
ps.speed("fastest")
ps.color("white")
ps.penup()
ps.setposition(courtWidth/2-450, courtHeight/2-300)

#writes some information for the user (manual)
man = Turtle(visible=False)
man.speed("fastest")
man.color("white")
man.penup()
man.setposition(courtWidth/2 - 1020, courtHeight/2-95)
man.write(" Move paddle- left and right\n\n Pause for 5 seconds- p\n\n Reset all scores- y", font = FONT2)

#gives the current ball speed
currSpeed = Turtle(visible=False)
currSpeed.speed("fastest")
currSpeed.color("white")
currSpeed.penup()
currSpeed.setposition(courtWidth/2 + 10, courtHeight/2 -20)
currSpeed.write("Current Ball Speed: " + str(ballSpeed), font = FONT3)

#writes scores to screen
def writeToScreen():
    global score, s, ballSpeed, averageScore, highScore, lowScore, avs, hs, ls
    f = open("scores.txt", "r+")
    
    avs.undo()
    avs.write("Average Score: " + str(averageScore), font = FONT) 
    hs.undo()
    hs.write("Highscore: " + str(highScore), font = FONT)
    ls.undo()
    ls.write("Lowscore: " + str(lowScore), font = FONT)    
    f.close()

#pulls from file to update the average, high, and low scores
def updateScores():
    global score, s, ballSpeed, averageScore, highScore, lowScore, avs, hs, ls
    f = open("scores.txt", "r+")
    f.write(str(score) + " ")
    for line in f:
        scoresInLine = line.split()
        scoresInLine = [int(x) for x in scoresInLine]
        averageScore = (sum(scoresInLine))//(len(scoresInLine))
        highScore = max(scoresInLine)
        lowScore = min(scoresInLine)
    f.close()
    
def draw_border(): #draws the border for the game
    border.pensize(3)
    border.penup()
    border.setposition(-courtWidth/2, -courtHeight/2)
    
    border.pendown()
    border.left(90)
    border.forward(courtHeight)
    
    border.goto(courtWidth/2, border.ycor())  
    border.backward(courtHeight)
    
def setBall(): #resets the ball to the middle of the screen
    
    ball.ht()
    ball.speed("fastest")
    ball.setposition(0,0)
    ball.setheading((0 + randint(-120,-10)))
    
    #resets ball speed and score. 
    #updates scores on screen
    global ballSpeed, s, score, avs, averageScore, hs, highScore, ls, lowScore
    ballSpeed = 6
    ball.st()
    ball.speed(ballSpeed)
    currSpeed.undo()
    currSpeed.write("Current Ball Speed: " + str(ballSpeed), font = FONT3)
    score = 0
    s.undo()
    s.write("Score: " + str(score), font = FONT)    
    writeToScreen()
    
    
def pLeft(): #moves the player left
    x = player.xcor()
    x -= playerSpeed
    if x> playerWidth/2 - courtWidth/2:
        player.setx(x)

def pRight(): #moves the player right
    x = player.xcor()
    x = x +playerSpeed
    if x < courtWidth/2 - playerWidth/2:
        player.setx(x)

def collision(t1, t2): #detects if the ball has hit the paddle
    distance = t1.distance(t2)
    global score, s, ballSpeed, averageScore, highScore, lowScore, avs, hs, ls
    if distance < playerWidth/2:       
        t2.setheading(0-t2.heading())
        t2.forward(ballSpeed)
        score += 1
        s.undo()
        s.write("Score: " + str(score), font = FONT)
        #saves each score to scores.txt file
        #finds the averageScore, highScore, and lowScore and writes to screen        
        updateScores()
        writeToScreen() 
                
        #increments ballSpeed by 2 every time ball hits paddle
        ballSpeed += 2
        currSpeed.undo()
        currSpeed.write("Current Ball Speed: " + str(ballSpeed), font = FONT3)
        
#erase all scores from file             
def hardReset():
    global score, s, averageScore, avs, highScore, hs, lowScore, ls
    f = open('scores.txt','r+')
    f.truncate(0)
    writeToScreen()   
    
#pauses for 5 seconds
def pause():
    ps.write("Paused", font = FONT)
    time.sleep(5)
    ps.undo()

#main
def move():
    global score, s, averageScore, avs, highScore, hs, lowScore, ls
    ball.forward(ballSpeed)
    x,y = ball.position()
    
    if y < -courtHeight/2:
        #saves each score to scores.txt file
        #finds the averageScore, highScore, and lowScore and writes to screen
        updateScores()
        writeToScreen()  
        score = 0
        s.undo()
        s.write("Score: " + str(score), font = FONT)        
        setBall()
    elif y > courtHeight/2 - turtleFactor:
        ball.setheading(-ball.heading())
    elif x > courtWidth/2 - turtleFactor:
        ball.setheading(180-ball.heading())
    elif x < turtleFactor - courtWidth/2:
        ball.setheading(180-ball.heading()) 
    else:
        collision(player, ball)
        
    screen.ontimer(move, 20) #every after twenty ms call the move() function
    
#screen
screen = Screen()
screen.title("Jakob's Pong")
screen.bgcolor("black")
screen.setup(width = 1.0, height = 1.0)


#Court Border
border = Turtle(visible = False)
border.speed("fastest")
border.color("white")
draw_border()

#setup ball
ball = Turtle("circle")
ball.penup()
ball.color("white")

#setup player paddle
player = Turtle("square")
player.penup()
player.sety(-courtHeight/2)
player.turtlesize(playerHeight/turtleFactor, playerWidth/turtleFactor)
player.color("white")


#start game
setBall()
move()

#inputs
screen.onkey(pRight, "Right") 
screen.onkey(pLeft, "Left")
screen.onkey(setBall, "r")
screen.onkey(hardReset, "y")
screen.onkey(pause, "p")


#check for inputs and loop the program
screen.listen()
screen.mainloop()