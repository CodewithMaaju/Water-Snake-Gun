    # Snake, water, Gun 
    # Snake vs Water: Snake wins
    # Water vs Gun: Water wins
    # Gun vs Snake: Gun wins
    # In case of tie, the game will be restarted.
a = input("Press Enter to start the game: ")
while True:
    print("\n------------------------")
    b = input("Enter your choice: Snake, Water, Gun: ")
    import random
    c = random.choice(["Snake", "Water", "Gun"])
    print("Computer's choice: ", c)
    if b == c:
        print("It's a tie. Restart the game \n\n")
    elif b == "Snake" and c == "Water":
        print("You win!")
        break
    elif b == "Water" and c == "Gun":
        print("You win!")
        break
    elif b == "Gun" and c == "Snake":
        print("You win!")
        break
    else:
        print("You lose! and computer wins.")
input("\nPress Enter to exit...")
