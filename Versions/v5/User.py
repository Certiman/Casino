"""
User - class

Manages the user during the running of any casino game.
- streak: int = 0
- times_won: int = 0
- highest_streak: list[int] = []
- highest_winnings: list[int] = []

Constructor: uses Repository to read the user data from JSON
- loadUser(rep:Repository)

Provides:
- updateMoneyAndStreak
- storeUserData(rep:Repository)
"""
class User:
    pass