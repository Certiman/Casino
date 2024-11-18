"""
CasinoGame - class

Manages the generic aspects of the games and the game loop.
- constructor: for a User calling this class, sets moneyWon = 0
- function playAgain(): asks whether game loop should be continued.
- function endGame(): shows end stats.
- abstract function winsMoney (money_won), defined by subclasses

Causes updates to User 
- update streak, times_won (if money_won > 0)

SubClasses:
- see games.py

"""
class CasinoGame():
    pass