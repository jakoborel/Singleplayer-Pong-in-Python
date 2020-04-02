from turtle import Turtle, Screen
from random import choice, randint
import time

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

#Initialize score,highscore,lowscore, and average scores and turtles
score = 0
s = Turtle(visible=False)
s.speed("fastest")
s.color("white")
s.penup()
s.setposition(-courtWidth/2, courtHeight-300)
s.write("Score: " + str(score), font = FONT)

highScore = 0
hs = Turtle(visible=False)
hs.speed("fastest")
hs.color("#28aa05")
hs.penup()
hs.setposition(-courtWidth + 550, courtHeight-300)
hs.write("Highscore: " + str(highScore), font = FONT)

lowScore = -1
ls = Turtle(visible=False)
ls.speed("fastest")
ls.color("#ba1e0d")
ls.penup()
ls.setposition(-courtWidth + 750, courtHeight-300)
ls.write("Lowscore: " + str(lowScore), font = FONT)


averageScore = 0
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

#writes scores to file
def updateFile(numOfGames, totalPoints, highestScore, lowestScore):
    f = open("pongData.txt", 'w')
    f.write(str(numOfGames) + ' ' + str(totalPoints) + ' ' + str(highestScore) + ' ' + str(lowestScore))

#writes scores to screen
def writeToScreen():
    global averageScore, highScore, lowScore, avs, hs, ls
    avs.undo()
    avs.write("Average Score: " + str(averageScore), font = FONT) 
    hs.undo()
    hs.write("Highscore: " + str(highScore), font = FONT)
    if lowScore == -1:
        ls.undo()
        ls.write("Lowscore: " + str(0), font = FONT)        
    else:
        ls.undo()
        ls.write("Lowscore: " + str(lowScore), font = FONT)    
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
    global ballSpeed, s, score
    global numOfGames, totalPoints, averageScore, highScore, lowScore    
    ball.ht()
    ball.speed("fastest")
    ball.setposition(0,0)
    ball.setheading((0 + randint(-120,-10)))
        
    ballSpeed = 6
    ball.st()
    ball.speed(ballSpeed)
    currSpeed.undo()
    currSpeed.write("Current Ball Speed: " + str(ballSpeed), font = FONT3)
    
    numOfGames += 1
            
    score = 0
    s.undo()
    s.write("Score: " + str(score), font = FONT)
    updateFile(numOfGames, totalPoints, highScore, lowScore)
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
    global score, s, ballSpeed, highScore, lowScore, numOfGames, totalPoints 
    if distance < playerWidth/2:       
        t2.setheading(0-t2.heading())
        t2.forward(ballSpeed)
        score += 1
        s.undo()
        s.write("Score: " + str(score), font = FONT)
        
        
        #increments ballSpeed by 2 every time ball hits paddle
        ballSpeed += 2
        currSpeed.undo()
        currSpeed.write("Current Ball Speed: " + str(ballSpeed), font = FONT3)
            
#erase all scores from file             
def hardReset():
    global score, s, averageScore, avs, highScore, hs, lowScore, ls, numOfGames, totalPoints
    f = open("pongData.txt", "r+")
    f.truncate()
    f.write("1 0 0 -1")
    f.close()
    f = open("pongData.txt",'r')
    numsInFile = f.read().split()
    f.close()
    numOfGames = int(numsInFile[0])
    totalPoints = int(numsInFile[1])
    highScore = int(numsInFile[2])
    lowScore = int(numsInFile[3]) 
    updateFile(numOfGames, totalPoints, highScore, lowScore)
    writeToScreen()   
    
#pauses for 5 seconds
def pause():
    ps.write("Paused", font = FONT)
    time.sleep(5)
    ps.undo()
    

def move():
    global score, s, averageScore, avs, highScore, hs, lowScore, ls, totalPoints, numOfGames

    ball.forward(ballSpeed)
    x,y = ball.position()
    
    if y < -courtHeight/2:
        #update scores in file and write to screen
        #check if score is -1 or less than the lowScore
        if lowScore == -1:
            lowScore = score
        elif score < lowScore:
            lowScore = score 
        #check if score is greater than highScore
        if score > highScore:
            highScore = score
        #set totalPoints and averageScore
        totalPoints += score
        averageScore = float("{0:.2f}".format(totalPoints/numOfGames))
            
        updateFile(numOfGames, totalPoints, highScore, lowScore)
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
    
    screen.ontimer(move, 5) #every after twenty ms call the move() function
#main
try:
    f = open("pongData.txt",'r')
    f.close()
except:
    #the file does not exist
    f = open("pongData.txt",'w')
    f.write('0 0 0 -1')
    f.close()

f = open("pongData.txt",'r')
numsInFile = f.read().split()
f.close()
numOfGames = int(numsInFile[0])
totalPoints = int(numsInFile[1])
highScore = int(numsInFile[2])
lowScore = int(numsInFile[3]) 

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