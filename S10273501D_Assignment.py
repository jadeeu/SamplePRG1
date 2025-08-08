import random

def player_information(player):
    print("\n--- Player Information ---")
    print(f"Name: {player['name']}")
    print(f"Gold Pieces (GP): {player['gp']}")
    print(f"Pickaxe Level: {player['pickaxe_level']}")
    print(f"Backpack Capacity: {player['backpack_capacity']}")
    print(f"Backpack Contents: {player['backpack']}")
    print(f"Day: {player['day']}")
    print(f"Steps Taken: {player['steps']}")
    print("--------------------------")

def show_town_menu(day, gp):
    print()
    print(f"DAY {day}   GP: {gp}")
    print("----- Sundrop Town -----")
    print("(B)uy stuff")
    print("See Player (I)nformation")
    print("See Mine (M)ap")
    print("(E)nter mine")
    print("Sa(V)e game")
    print("(Q)uit to main menu")
    print("------------------------")
    choice = input("Your choice? ").strip().lower()
    return choice

def show_shop_menu(gp, pickaxe_level, backpack_capacity):
    print("----------------------- Shop Menu -------------------------")
    if pickaxe_level == 1:
        print("(P)ickaxe upgrade to Level 2 to mine silver ore for 50 GP")
    elif pickaxe_level == 2:
        print("(P)ickaxe upgrade to Level 3 to mine gold ore for 150 GP")
    
    if backpack_capacity == 10:
        print("(B)ackpack upgrade to carry 12 items for 20 GP")
    elif backpack_capacity == 12:
        print("(B)ackpack upgrade to carry 15 items for 50 GP")
    
    print("(L)eave shop")
    print("-----------------------------------------------------------")
    print(f"GP: {gp}")
    print("-----------------------------------------------------------")
    
    choice = input("Your choice? ").strip().lower()
    return choice

def buy_item(choice, gp, pickaxe_level, backpack_capacity):
    if choice == 'p':
        if pickaxe_level == 1 and gp >= 50:
            gp -= 50
            pickaxe_level = 2
            print("Pickaxe upgraded to Level 2!")
        elif pickaxe_level == 2 and gp >= 150:
            gp -= 150
            pickaxe_level = 3
            print("Pickaxe upgraded to Level 3!")
        else:
            print("Not enough GP or already max level.")
    
    elif choice == 'b':
        if backpack_capacity == 10 and gp >= 20:
            gp -= 20
            backpack_capacity = 12
            print("Backpack upgraded to 12 slots!")
        elif backpack_capacity == 12 and gp >= 50:
            gp -= 50
            backpack_capacity = 15
            print("Backpack upgraded to 15 slots!")
        else:
            print("Not enough GP or already max size.")
    
    return gp, pickaxe_level, backpack_capacity

def start_new_game():
    name = input("Greetings, miner! What is your name? ")
    print(f"Pleased to meet you, {name}. Welcome to Sundrop Town!")

    player = {
        "name": name,
        "gp": 0,
        "pickaxe_level": 1,
        "backpack_capacity": 10,
        "backpack": {"copper": 0, "silver": 0, "gold": 0},
        "load": 0,
        "day": 1,
        "steps": 0,
        "turns_left": 20,
        "position": (0, 0),
        "portal_position": (0, 0),
    }

    town_loop(player)

def town_loop(player):
    while True:
        choice = show_town_menu(player["day"], player["gp"])

        if choice == 'b':
            while True:
                shop_choice = show_shop_menu(player["gp"], player["pickaxe_level"], player["backpack_capacity"])
                if shop_choice == 'l':
                    break
                player["gp"], player["pickaxe_level"], player["backpack_capacity"] = buy_item(
                    shop_choice, player["gp"], player["pickaxe_level"], player["backpack_capacity"]
                )
        elif choice == 'i':
            player_information(player)
        elif choice == 'm':
            print("\n Mine map will be displayed here. (Coming soon...)")
        elif choice == 'e':
            print("\n Entering the mine... (Coming soon...)")
            break
        elif choice == 'v':
            print("\n Game saved! (Coming soon...)")
        elif choice == 'q':
            print("\nReturning to main menu...")
            return
        else:
            print("Invalid choice. Try again.")

def load_game():
    print("Loading game... (not implemented yet)")

def main_menu():
    print("---------------- Welcome to Sundrop Caves! ----------------")
    print("You spent all your money to get the deed to a mine, a small")
    print("backpack, a simple pickaxe and a magical portal stone.")
    print()
    print("How quickly can you get the 500 GP you need to retire")
    print("and live happily ever after?")
    print("-----------------------------------------------------------")
    print("--- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
    print("(Q)uit")
    print("------------------")

    choice = input("Your choice? ").strip().lower()

    if choice == 'n':
        start_new_game()
    elif choice == 'l':
        load_game()
    elif choice == 'q':
        print("Thanks for playing Sundrop Caves!")
    else:
        print("Invalid choice. Try again.")
        main_menu()

# Start the game
main_menu()
