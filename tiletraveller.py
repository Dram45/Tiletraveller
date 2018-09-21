#Tiletraveller
#Travel within 3x3 grid with several paths walled off
#As for possible input if starting in spot 1.1 only one path is available
#show possible paths, check if walls are implemented before showing and if none add that as a move option
#if move is valid, move there and show new options.
#gitrepository = https://github.com/Dram45/Tiletraveller.git

MINX = 1
MAXX = 3
MINY = 1 
MAXY = 3
victory = False
currentpositionx = 1
currentpositiony = 1
validmoves = {'n'}
validmoveslength = len(validmoves)
print(validmoveslength)

move = input("Direction: ")
move = move.lower()

allowedmove = False
while allowedmove == False:
    if move not in validmoves:
        print("Not a valid direction")
        move = input("Direction: ")
    if move in validmoves:
        allowedmove = True
while victory == False:
    if move == 'n':
        currentpositionx += 1
    if move == 's':
        currentpositionx -= 1
    if move == 'w':
        currentpositiony -= 1
    if move == 'e':
        currentpositiony += 1
    

if currentpositionx == 1 and currentpositiony == 1:
    validmoves = {'n'}
if currentpositionx == 1 and currentpositiony == 2:
    validmoves = {'n','s','e'}
if currentpositionx == 1 and currentpositiony == 3:
    validmoves = {'s', 'e'}
if currentpositionx == 2 and currentpositiony == 1:
    validmoves = {'n'}
if currentpositionx == 2 and currentpositiony == 2:
    validmoves = {'w','s'}
if currentpositionx == 2 and currentpositiony == 3:
    validmoves = {'w','e'}
if currentpositionx == 3 and currentpositiony == 1:
    victory = True
if currentpositionx == 3 and currentpositiony == 2:
    validmoves = {'n', 's'}
if currentpositionx == 3 and currentpositiony == 3:
    validmoves = {'w', 's'}
