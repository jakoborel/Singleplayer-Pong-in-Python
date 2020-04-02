def updateFile(fileName, numOfGames, totalPoints, highestScore, lowestScore):
    f = open(fileName, 'w')
    f.write(str(numOfGames) + ' ' + str(totalPoints) + ' ' + str(highestScore) + ' ' + str(lowestScore))

#main program
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
highestScore = int(numsInFile[2])
lowestScore = int(numsInFile[3])



