def begin():
    print ("Welcome to the Carnival!")
    answer1 = input("Now that you're here, what will you do first?\n1. Get Hawaiian shaved ice\n2. Go on a ride\n3. See a show at the big top\n4. Walk around aimlessly\n")
    if answer1 == "1":
        shavedIce()
    elif answer1 == "2":
        goOnRide()
    elif answer1 == "3":
        bigTop()
    elif answer1 == "4":
        walkAround()
    else:
        print("Sorry but that's not an option, try again\n\n\n")
        begin()
def shavedIce():
    answer2 = input("Nice choice, what flavor will you get?\n1. Pina Colada\n2. Strawberry\n3. Cotton Candy\n")
    if answer2 == "1":
        pinaColada()
    elif answer2 == "2":
        strawberry()
    elif answer2 == "3":
        cottonCandy()
    else:
         print("Sorry but that's not an option, try again\n\n\n")
         shavedIce()
def pinaColada():
    print("GAME OVER\nTurns out you have a severe pineapple alergy, you're quickly rushed to a hospital\nLooks like your day at the carnival is over\nBetter luck next time\n\n\n")
    begin()
def strawberry():
    answer3 = input("Yum! What will you do next?\n1. Go on a ride\n2. See a show at the big top\n3. Walk around aimlessly\n")
    if answer3 == "1":
        goOnRide()
    elif answer3 == "2":
        bigTop()
    elif answer3 == "3":
        walkAround()
    else:
         print("Sorry but that's not an option, try again\n\n\n")
         strawberry()
def cottonCandy():
    answer4 = input("Good decision, I've heard about some shady things going on with their pina colada flavor. What will you do next?\n1. Go on a ride\n2. See a show at the big top\n3. Walk around aimlessly\n")
    if answer4 == "1":
        goOnRide()
    elif answer4 == "2":
        bigTop()
    elif answer4 == "3":
        walkAround()
    else:
         print("Sorry but that's not an option, try again\n\n\n")
         cottonCandy()
def goOnRide():
    print("Cool, tickets were included with your admission to the park")
    answer5 = input("What ride do you want to go on?\n1. Zero Gravity\n2. Ferris Wheel\n3. Mad Mouse\n4. Tilt-A-Whirl")
    if answer5 == "1":
        zeroGravity()
    elif answer5 == "2":
        ferrisWheel()
    elif answer5 == "3":
        madMouse()
    elif answer5 == "4":
        tiltAWhirl()
    else:
        print("Sorry but that's not an option, try again\n\n\n")
        goOnRide()
def  zeroGravity():
    print("You walk up to the bored looking teen running the ride and they let you through\n after a minute of being plastered to a wall and spinning you think you've had enough rides for one night adn decide to do something else for a bit")
    answer6 = input("What next?\n1. Get Hawaiian Shaved Ice\n2. See a show at the Big Top\n3. Walk around aimlessly\n")
    if answer6 == "1":
        shavedIce()
    elif answer6 == "2":
        bigTop()
    elif answer6 == "3":
        walkaround()
    else:
        print("Sorry but that's not an option, try again")
        zeroGravity()
def ferrisWheel():
    print("its a long wait and you're kind of bored")
    answer7 = input("Do you want to\n1. play games on you're phone\n2. Go do something else (You dont have time for lines)\n3. Talk to someone else in line")
    if answer7 == "1":
        gamesDean()
    elif answer7 == "2":
        impatience()
    elif answer7 == "3":
        goodEndingfrfr()
    else:
        print("Sorry but that's not an option, try again")
        ferrisWheel()
def gamesDean():
    print("You start playing you're new favorite game TETRIS and you're on youre way to a new highscore, you can feel it in the air")
    print("You're so focused on getiing your new high score that you hardly even notice the line moving forward, in no time you're on the ferris wheel and not seeing a thing because this is your best ever TETRIS gameplay")
    print("YOU GOT YOUR HIGHSCORE!you also missed the firework show, but it's fine. You decide that today has been successful and return home")
    begin()
def impatience():
    answer9 = input("Jeez man you cant just wait for a couple minutes? all right then where are you heading?\n1. Get Hawaiian Shaved Ice\n2. See a show at the Big Top\n3. Walk around aimlessly\n")
    if answer9 == "1":
        shavedIce()
    elif answer9 == "2":
        bigTop()
    elif answer9 == "3":
        walkaround()
    else:
        print("Sorry but that's not an option, try again")
        impatience()
def goodEndingfrfr():
    print("Best decision ever! You start a conversation with the person just in front of you. You guys immediately connect and decide to buddy up for the ride. You exchanged phone numbers and you got to the top of the ferris wheel right as the firework show started. It was at this point in time that you worked up the courage to ask them on a date. Flash forward a few months and you're the happiest you've ever been and you're meeting their family. Flash forward a couple more years and you're getting married to them, You live a long and happy life with them\n\n\nCongrats and good luck in your next playthrough")
    begin()
def madMouse():
    answer10 = input("ugh the mad mouse line is always so slow, but it's well worth it for those terrifying turns where it feels like the wheels are off the tracks! Now that you have a slight headache and feel a bit queasy what will you do next?\n1. Get Hawaiian Shaved Ice\n2. See a show at the Big Top\n3. Walk around aimlessly\n")
    if answer10 == "1":
        shavedIce()
    elif answer10 == "2":
        bigTop()
    elif answer10 == "3":
        walkaround()
    else:
        print("Sorry but that's not an option, try again")
        madMouse()
def tiltAWhirl():
    print("GAME OVER\nAs you were enjoying your time on your favorite ride you unexpectadly spin really fast. Long story short your head slamed back and now you have a minor concussion. You return home from the carnival completly exahausted and immedialty go to sleep")
    begin()
def bigTop():
    answer11 = input("")
begin()