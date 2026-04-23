# Have game open
# Present title card and instructions
# Start game loop
# End game loop when player wins, loses, or quits
# Display win/lose message 
# Exit game

def title_screen():
    print("Brains and Brownies: A Zombie Fighting Game")
    to_start = input("Press Enter to start the game...")
    to_quit = input("Press Q to quit the game...")
    if to_quit.lower() == 'q':
        exit()
    if to_start == '':
        print("In this game, you will fight off waves of zombies. Defeat all the zombies to win!")
    if to_start and to_quit.lower() != 'q':
        print("Invalid input. Please try again.")
        title_screen()