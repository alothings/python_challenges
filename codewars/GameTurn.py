# Terminal game turn function

# Create text-based terminal of board game
# Each person has 6 steps. In the following order
# Roll dice, move, combat, get coins, buy health, and print.

# calls the functions in the proper order as described
def do_turn():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()

# Another function
def do_turn():
    steps = [roll_dice, move, combat,
             get_coins, buy_health, print_status]

    for step in steps:
        step()