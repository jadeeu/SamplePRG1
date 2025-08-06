player = {
    "name": "Cher",
    "gp": 0,
    "pickaxe_level": 1,     # 1 = copper, 2 = silver, 3 = gold
    "backpack_capacity": 10,
    "backpack": {"copper": 0, "silver": 0, "gold": 0},
    "load": 0,
    "day": 1,
    "steps": 0,
    "turns_left": 20,
    "position": (0, 0),     # (row, col)
    "portal_position": (0, 0),
}
print("---------------- Welcome to Sundrop Caves! ----------------")
print("You spent all your money to get the deed to a mine, a small")
print("  backpack, a simple pickaxe and a magical portal stone.")
print()
print("How quickly can you get the 500 GP you need to retire")
print("  and live happily ever after?")
print("-----------------------------------------------------------")

day = 1

def show_town_menu():
    print()
    print(day)
    print("----- Sundrop Town -----")
    print("(B)uy stuff")
    print("See Player (I)nformation")
    print("See Mine (M)ap")
    print("(E)nter mine")
    print("Sa(V)e game")
    print("(Q)uit to main menu")
    print("------------------------")

def show_main_menu():
    print()
    print("--- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
#    print("(H)igh scores")
    print("(Q)uit")
    print("------------------")

print('----------------------- Shop Menu -------------------------')
print('(P)ickaxe upgrade to Level 2 to mine silver ore for 50 GP')
print('(B)ackpack upgrade to carry 12 items for 20 GP')
print('(L)eave shop')
print('-----------------------------------------------------------')
