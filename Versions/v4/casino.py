"""Main Casino File"""

# --> Version 4 Changelog <--
# Pylinted the code (im not going to do this again, it took me ~3 hours)
# Added Sleeps to make the game more readable and easier to understand
# Made the settings file more readable and easier to understand
# Added obfuscation to the save function (no more cheating by changing the save file)

from time import sleep
import games
from utils import welcome, bet, clear, bye, LOST
from settings import settings_main, save

# Outer game loop
while 1:
    # Initialize the game settings for every new game
    streak: int = 0
    times_won: int = 0
    highest_streak: list[int] = []
    highest_winnings: list[int] = []
    all_games: list[str] = [
        "Number Guesser",
        "Roulette",
        "Slots",
        "Blackjack",
        "Baccarat",
    ]

    money, user = settings_main()
    # Inner game loop
    while 1:
        game = input(welcome(user)) or "0"

        if "quit" in game:
            break

        if game == "0":
            continue

        if game == all_games[0] or int(game) == 1:
            Chosen_game = games.guesser
            GI = 0

        elif game == all_games[1] or int(game) == 2:
            Chosen_game = games.roulette
            GI = 1

        elif game == all_games[2] or int(game) == 3:
            Chosen_game = games.slots
            GI = 2

        elif game == all_games[3] or int(game) == 4:
            Chosen_game = games.blackjack
            GI = 3

        elif game == all_games[4] or int(game) == 5:
            Chosen_game = games.baccarat
            GI = 4

        # Initialize game

        print()
        print(f"You have chosen to play {all_games[GI]}!")

        money, money_betting = bet(money)
        sleep(3)
        clear()
        money_won, streak, times_won = Chosen_game(money_betting, streak, times_won)
        sleep(5)
        money = money + money_won
        highest_winnings.append(money_won)
        highest_streak.append(streak)

        save(money, user)

        sleep(3)
        clear()

        # LOSE
        if money == 0:
            print(LOST)
            print(bye(highest_streak, highest_winnings, times_won))
            sleep(10)
            clear()
            break

        print()
        print(f"You now have {money}$ and are on a streak of {streak}")

        # Run again in the current profile
        print()
        again = input("Play a new game? (y/n): ")
        if "y" in again:
            print("Ok! Clearing terminal for easier view!")
            sleep(3)
            clear()
            continue
        if "n" in again:
            print()
            print(f"When you come back next time you will start with {money}$")
            sleep(3)
            print(bye(highest_streak, highest_winnings, times_won))
            sleep(10)
            clear()
            break
        continue

    if not "n" in again: # only ask to restart the game when the person has lost (has 0 dollars).
        # Restart the game
        restart = input("Do you want to replay (on a new profile)? (y/n): ")
        if "y" in restart:
            print("Ok! Clearing terminal for easier view!")
            sleep(3)
            clear()
            continue
        if "n" in restart:
            print("Thank you for playing! Have a great day!")
            sleep(3)
            clear()
            break
        continue