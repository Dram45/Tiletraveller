#Tiletraveller
#Travel within 3x3 grid with several paths walled off
#As for possible input if starting in spot 1.1 only one path is available
#show possible paths, check if walls are implemented before showing and if none add that as a move option
#if move is valid, move there and show new options.
#gitrepository = https://github.com/Dram45/Tiletraveller.git

def printvalidmoves(l1):
    mainstring = str("You can travel: ")
    counter = 0
    for chars in l1:
        if counter >= 1 and counter < len(l1):
            mainstring = mainstring + " or "
        if chars == 'n':
            mainstring = mainstring + "(N)orth"
        elif chars == 'e':
            mainstring = mainstring + "(E)ast"
        elif chars == 's':
            mainstring = mainstring + "(S)outh"

        elif chars == 'w':
            mainstring = mainstring + "(W)est"
        counter += 1
    mainstring = mainstring + "."

    print(mainstring)
    return

def move(l1):
    move = input("Direction: ")
    move = move.lower()
    allowedmove = False
    while allowedmove == False:
        if move not in validmoves:
            print("Not a valid direction!")
            move = input("Direction: ")
            move = move.lower()
        if move in validmoves:
            allowedmove = True
    return move
def changepos(m,x,y):

    if m == 'n':
        x += 1
        return x, y
    if m == 's':
        x -= 1
        return x,y
    if m == 'w':
        y -= 1
        return x,y
    if m == 'e':
        y += 1
        return x,y
    

def checkwalls(s1, s2):
    
    if s2 == 1 and s1 == 1:
        valid = ['n']
        return valid
    if s2 == 1 and s1 == 2:
        valid = ['n','e','s']
        return valid
    if s2 == 1 and s1 == 3:
        valid =  ['e', 's']
        return valid
    if s2 == 2 and s1 == 1:
        valid = ['n']
        return valid
    if s2 == 2 and s1 == 2:
        valid = ['s','w']
        return valid
    if s2 == 2 and s1 == 3:
        valid = ['e','w']
        return valid
    if s2 == 3 and s1 == 1:
        valid = ['Victory']
        return valid
    if s2 == 3 and s1 == 2:
        valid = ['n', 's']
        return valid
    if s2 == 3 and s1 == 3:
        valid = ['s', 'w']
        return valid

def checkvictory(tf):
    if 'Victory' in tf:
        return True
    return False


victory = False
currentpositionx = 1
currentpositiony = 1
validmoves = ['n']

while victory == False:
   
    printvalidmoves(validmoves)
    movement = move(validmoves)
    currentpositionx, currentpositiony = changepos(movement,currentpositionx,currentpositiony)
    validmoves = checkwalls(currentpositionx, currentpositiony)
    victory = checkvictory(validmoves)

    


print("Victory!")