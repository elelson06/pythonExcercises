"""
Description:

The "Score Tracker Game" is a program designed to manage and track scores for a multiplayer game. 
It offers a user-friendly interface with two main menus: the Initial Menu allows users to load players and start the game, 
while the Main Menu enables users to input scores for each round, view standings, remove players, and finally, end the game.

The program ensures that a minimum number of players are loaded before starting the game. As the game progresses, 
it keeps a record of players' scores, provides real-time standings, and maintains a detailed history of each player's performance in every round. 
Players can be removed from the game if necessary, and the program announces the winner at the end of the game.

The "Score Tracker Game" is a useful tool for various multiplayer games, from board games to sports tournaments, 
making it easy to keep track of scores and monitor the progress of each player throughout the game.
"""

# Define the Game Menus
initialMenu = '''
    Select an option:
    1 - Load Players (enter 'exit' to finish)
    2 - Start Game
    3 - Exit
'''
mainMenu = '''
    Select an option:
    1 - Load scores for a new round
    2 - View standings
    3 - Remove a player
    4 - End Game
'''

# Define the dictionaries and variables we'll need
records = {}
eliminatedPlayers = {}
rounds = 0
# To validate the minimum conditions to start a game
# In this case, we'll only check that at least 2 players have been loaded
minimumData = True
# Variable to store the user's selection for each menu
initialMenuSelection = 0
mainMenuSelection = 0
# Flags to indicate which menu should be shown
initialMenuActive = True
mainMenuActive = False

# Show the Initial Menu while it's active
while initialMenuActive:
    initialMenuSelection = int(input(initialMenu))
    # A simple validation to handle unexpected inputs
    if initialMenuSelection not in (1, 2, 3):
        print("Incorrect option! Please try again!\n")

    # For option 1 - Load Players
    if initialMenuSelection == 1:
        continueInput = True
        while continueInput:
            name = input("Enter Player's Name (or 'exit' to finish): ")
            if name.lower() == "exit":
                continueInput = False
            else:
                # Initialize the score with value 0
                records[name] = 0
    # For option 2 - Start the game
    elif initialMenuSelection == 2:
        # Validate the minimum required to start the game
        if len(records) > 1:
            initialMenuActive = False
            mainMenuActive = True
            # Create a history dictionary based on the records dictionary (only with names)
            history = {key: [] for key in records.keys()}
        else:
            print("At least 2 Players are required to start a game.")
    elif initialMenuSelection == 3:
        # Deactivate the initialMenu and greet without showing the mainMenu
        initialMenuActive = False
        print("Goodbye!")

while mainMenuActive:
    # Show the Main Menu
    mainMenuSelection = int(input(mainMenu))
    # A simple validation to handle unexpected inputs
    if mainMenuSelection not in (1, 2, 3, 4):
        print("Incorrect option! Please try again!\n")

    # Option 1: Load scores for the current round
    if mainMenuSelection == 1:
        print("Enter the scores obtained by each participant:")
        rounds += 1
        for player in records.keys():
            # Register the score in both dictionaries
            print(player, ": ")
            points = int(input())
            records[player] += points
            history[player].append({"round": rounds, "points": points})
    # Option 2: View standings
    elif mainMenuSelection == 2:
        print("Standings Table:")
        # Sort from highest to lowest based on score
        for position in sorted(records, key=records.get, reverse=True):
            print(position, "  ", records[position], "Pts.")
    # Option 3: Remove a player. In case someone withdraws early, and we don't need
    #           to ask for their score in the following rounds
    elif mainMenuSelection == 3:
        playerToRemove = input("Enter the name of the player you want to remove: ")
        # Check if the entered name corresponds to one of the players
        if playerToRemove not in records.keys():
            print("The entered player was not found!")
        else:
            # Remove the player and get their score to display it
            eliminatedPlayers[playerToRemove] = records.pop(playerToRemove)
            print(playerToRemove, "has been removed from the game! (Pts: ", str(eliminatedPlayers[playerToRemove]), ")")
    # Option 4: End of the game. Message and summary with the winner, standings, and the history
    #           of points for each round per player
    elif mainMenuSelection == 4:
        mainMenuActive = False
        print(" ------------------------------------------------ ")
        print("|              End of the Game!                  |")
        print(" ------------------------------------------------ ")
        print("\t Winner -> ** ", max(records, key=records.get).upper(), " **")
        print("\t Scores Table:")
        for position in sorted(records, key=records.get, reverse=True):
            print("\t", position, "  ", records[position], "Pts.")
        print("\n\t History of played rounds:")
        for player, data in history.items():
            print(player, " ->  ", data)
