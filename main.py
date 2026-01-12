import random as rand
from time import sleep

users = []

# Functions relating to checking the user array, adding users, removing users, listing users, and their respective terminal menus.
def checkifArrayIsNull(userarray):
    if len(userarray) <= 1:
        print("There is not enough users. You need at least 2 to play.")
        return True
    else:
        return False

def checkuser(userarray, username):
    for user in userarray:
        if user.casefold() == username.casefold():
            return user
    return False

def adduser(userarray, username):
    formattedUser = username.strip()
    userarray.append(formattedUser)
    print("User added.")

def addMenu(userarray):
    print("Enter a user to add. To quit, enter 'x'")
    while True:
        username = input()
        if username == "x" or username == "X":
            break
        adduser(userarray, username)


def removeuser(userarray, username):
    bufferUser = checkuser(userarray, username)
    if bufferUser != False:
        userarray.remove(bufferUser)
        print(bufferUser, "removed.")
    else:
        print("User not found. Try again.")

def removeMenu(userarray):
    print("Enter a user to remove. To quit, enter 'x'")
    while True:
        username = input()
        if username == "x" or username == "X":
            break
        removeuser(userarray, username)

def listusers(userarray, listChoice):
    if listChoice == "list":
        for user in userarray:
            print(user)
            divider()
    else:
        for user in userarray:
            print(user, end=", ")


# Gun related functions.
def shootGun():
    print("Spinning the revolver...")
    bullet = revolverspin()
    randomChamber = revolverspin()
    print("Shooting...")
    sleep(3)
    if bullet == randomChamber:
        print("Bang!")
        return True
    print("Click!")
    return False


def revolverspin():
    return rand.randint(1,6)


# Rounds and Autoplay functions.
def oneround(userarray):
    randomUserList = userarray.copy()
    rand.shuffle(randomUserList)
    for user in randomUserList:
        if len(userarray) == 1:
            print(user, "has won!")
            divider()
            return True
        isBroOkay = shootGun()
        if isBroOkay:
            print(user, "has died. (skill issue)")
            continueChoice = input("Do you want to continue? (y/n) ")
            if continueChoice == "n":
                return "n"
            divider()
            users.remove(user)
            break
        else:
            print(user, "survived. (big amounts of aura)")
            divider()
    print("There are", len(userarray), "people remaining:", end=" ")
    listusers(userarray, listChoice="regular")
    print()
    return

def autoplay(userarray):
    roundCount = 1
    if checkifArrayIsNull(userarray) == True:
        return
    while True:
        print("Round", roundCount)
        divider()
        if oneround(userarray) == True or oneround(userarray) == "n":
            return
        else:
            roundCount += 1


def divider():
    print("-------------------------")


def mainmenu(userarray):
    while True:
        print("Welcome to Russian Roulette, Jacob Jones. Here are your options:")
        print("1 - Play one round. 2 - Play automatically. 3 - Add user. 4 - Remove user. 5 - Display users.")
        choice = input()
        match choice:
            case "1":
                oneround(userarray)
            case "2":
                autoplay(userarray)
            case "3":
                addMenu(userarray)
            case "4":
                removeMenu(userarray)
            case "5":
                listusers(userarray, listChoice="list")



mainmenu(users)