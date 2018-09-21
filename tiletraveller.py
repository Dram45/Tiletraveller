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
validmoves = ['n']



while victory == False:
    mainstring = str("You can travel: ")
    counter = 0
    for chars in validmoves:
        if counter >= 1 and counter < len(validmoves):
            mainstring = mainstring + " or "
        if chars == 'n':
            mainstring = mainstring + "(N)orth"
        elif chars == 's':
            mainstring = mainstring + "(S)outh"
        elif chars == 'e':
            mainstring = mainstring + "(E)ast"
        elif chars == 'w':
            mainstring = mainstring + "(W)est"
        counter += 1
    mainstring = mainstring + "."

    print(mainstring)
    mainstring = str("You can travel: ")

    move = input("Direction: ")
    move = move.lower()

    allowedmove = False
    while allowedmove == False:
        if move not in validmoves:
            print("Not a valid direction")
            move = input("Direction: ")
        if move in validmoves:
            allowedmove = True

    if move == 'n':
        currentpositionx += 1
    if move == 's':
        currentpositionx -= 1
    if move == 'w':
        currentpositiony -= 1
    if move == 'e':
        currentpositiony += 1    

    if currentpositiony == 1 and currentpositiony == 1:
        validmoves = ['n']
    if currentpositiony == 1 and currentpositionx == 2:
        validmoves = ['n','s','e']
    if currentpositiony == 1 and currentpositionx == 3:
        validmoves =  ['s', 'e']
    if currentpositiony == 2 and currentpositionx == 1:
        validmoves = ['n']
    if currentpositiony == 2 and currentpositionx == 2:
        validmoves = ['w','s']
    if currentpositiony == 2 and currentpositionx == 3:
        validmoves = ['w','e']
    if currentpositiony == 3 and currentpositionx == 1:
        victory = True
        break
    if currentpositiony == 3 and currentpositionx == 2:
        validmoves = ['n', 's']
    if currentpositiony == 3 and currentpositionx == 3:
        validmoves = ['w', 's']

print("Victory!")