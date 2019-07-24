playername = raw_input("Player 1, what is your name?")

playermove1 = raw_input(playername + "THE DRAGON IS CHASING YOU. Would you like to HIDE or RUN?")

if playermove1 == "run":
    playermove2a = raw_input("You ran away! Now, would you like to find FOOD or SHELTER?")
    if playermove2a == "food":
        playermove3a = raw_input("You found red berries. Would you like to eat them; YES or NO?")
        if playermove3a == "no":
            playermove4a = raw_input("You are still hungry. Would you like to find SHELTER or HUNT the dragon?")
            if playermove4a == "shelter":
                playermove5a = raw_input("You only find a narrow cave. Would you like to ENTER or find ELSE?")
                if playermove5a == "enter":
                    playermove6a = raw_input("You discover the cave is empty and decided to stay. Would you like to build a fire; YES or NO?")
                    if playermove6a == "no":
                        print("You went crazy through the dark night. YOU DIED")
                    if playermove6a == "yes":
                        print("The rescue team saw your smoke and found you. YOU SURVIVED.")
                if playermove5a == "else":
                    playermove6b = raw_input("Would you like to CREATE smoke signals or HUNT the dragon.")
                    if playermove6b == "create":
                        print("The rescue team saw your smoke and found you. YOU SURVIVED.")
                    if playermove6b == "hunt":
                        print("You find the dragon sleeping. He wakes up and kills you. YOU DIED.")
            if playermove4a == "hunt":
                print("You find the dragon sleeping. He wakes up and kills you. YOU DIED.")
        if playermove3a == "yes":
            print("The berries were poisonous. YOU DIED.")
    if playermove2a == "shelter":
        playermove3b = raw_input("You only find a narrow cave. Would you like to ENTER or find ELSE?")
        if playermove3b == "enter":
            playermove4c = raw_input("You discover the cave is empty and decided to stay. Would you like to build a fire; YES or NO?")
            if playermove4c == "no":
                print("You went crazy through the dark night. YOU DIED")
            if playermove4c == "yes":
                print("The rescue team saw your smoke and found you. YOU SURVIVED.")
        if playermove3b == "else":
            playermove4d = raw_input("Would you like to CREATE smoke signals or HUNT the dragon.")
            if playermove4d == "create":
                print("The rescue team saw your smoke and found you. YOU SURVIVED.")
            if playermove4d == "hunt":
                print("You find the dragon sleeping. He wakes up and kills you. YOU DIED.")
if playermove1 == "hide":
    print("The dragon found you. He eats you. YOU DIED.")
