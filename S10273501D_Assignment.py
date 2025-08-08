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
        show_town_menu(player["day"])
        choice = input("Your choice? ").strip().lower()

        if choice == 'b':
            print("\n🪙 Welcome to the shop! (Coming soon...)")
        elif choice == 'i':
            player_information(player)
        elif choice == 'm':
            print("\n🗺 Mine map will be displayed here. (Coming soon...)")
        elif choice == 'e':
            print("\n⛏ Entering the mine... (Coming soon...)")
            break  # Breaks out of town menu loop when entering the mine
        elif choice == 'v':
            print("\n💾 Game saved! (Coming soon...)")
        elif choice == 'q':
            print("\nReturning to main menu...")
            return  # Goes back to main menu
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

import random

prices = {
    "copper": random.randint(1, 3),
    "silver": random.randint(5, 8),
    "gold": random.randint(10, 18)
}