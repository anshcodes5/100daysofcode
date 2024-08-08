print("Welcome to Train Aventure!\n")
user_input1 = input('Type: "Start" to play.\nPress "Enter" to quit.\n\n').lower()

if user_input1 == "start":
    print("Game Starts:\n")
    print("You are at a Train Station")
    print("Train no. 1 is going to the left where you can see beautiful water lands.")
    print("Train no. 2 is going to the right where you can see snowy mountains.")
    opted1 = input("Where do you wanna go? Type \"1\" for Train no. 1 and type \"2\" for Train no. 2.\n")
    if opted1 == "1":
        print("The train left you at a beautiful water land, you can see vibrant blue water all around you.")
        opted1p1 = input('"D" to dive into the water.\n"W" to keep walking.\n').lower()
        if opted1p1 == "d":
            print("Game over! water was full of Sharks.")
        elif opted1p1 == "w":
             print("You see a water slide, an old cottage and a tunnel.")
             opted1p2 = input('"S\" to slide down the slide.\n\"E\" to enter the old cottage.\n"T" to enter the Tunnel.\n').lower()
             if opted1p2 == "s":
                 print("You win! The water slide slid you down into a sea of precious stones.")
             elif opted1p2 == "t":
                 print("Game over, the tunnel was full of white bears.")
             else:
                 print("Game over, the cottage was fool of ghosts.")
    else:
        print("The train left you at a beautiful cold snowy valley, you can see a warm jacket nearby.")
        opted2 = input('"P" to pick up the jacket.\n"C" to leave and continue walking.\n').lower()
        if opted2 == "p":
            print("You wore the jacket and walked ahead all warm and cozy, and see a gate, a cave and a wooden house.")
            opted2p1 = input('"G" to enter the gate.\n"C" to enter the cave.\n"W" to enter the wooden house.\n').lower()
            if opted2p1 == "g":
                print("You win! gate opened to a beautiful city full of warm and welcoming people")
            elif opted2p1 == "w":
                 print("You win! the wooden house was full of precious gems.")
            else:
                print("Game over, the cave was full of beasts.")
        else:
            print("Game over! you keep Walking without warm cloths and die of cold.")
else:
    input("Press enter to exit.")