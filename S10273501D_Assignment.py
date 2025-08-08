import json
import os
def display_intro_and_main_menu():
    print("---------------- Welcome to Sundrop Caves! ----------------")
    print("You spent all your money to get the deed to a mine, a small")
    print("backpack, a simple pickaxe and a magical portal stone.")
    print("How quickly can you get the 500 GP you need to retire")
    print("and live happily ever after?")
    print("-----------------------------------------------------------")
    print("--- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
    print("(Q)uit")
    print("------------------")

def save_game(player):
    filename = f"{player['name']}_save.json"
    try:
        with open(filename, "w") as f:
            json.dump(player, f, indent=4)
        print(f"Game saved successfully as '{filename}'.")
    except IOError as e:
        print(f"Error saving game: {e}")

def load_game():
    save_files = [f for f in os.listdir() if f.endswith("_save.json")]
    if not save_files:
        print("No saved games found.")
        return None

    print("Saved games:")
    for idx, file in enumerate(save_files, 1):
        print(f"{idx}. {file}")

    choice = input("Enter the number of the saved game to load: ").strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(save_files):
        print("Invalid choice.")
        return None

    filename = save_files[int(choice) - 1]
    try:
        with open(filename, "r") as f:
            player = json.load(f)
        print(f"Loaded game for player {player['name']}.")
        return player
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading game: {e}")
        return None
    
def new_game():
    name = input("Greetings, miner! What is your name? ").strip()
    player = {
        "name": name,
        "day": 1,
        "gp": 0,
        "pickaxe_level": 1,
        "backpack_capacity": 10,
        "backpack": {"copper": 0, "silver": 0, "gold": 0}
    }
    print(f"Pleased to meet you, {name}. Welcome to Sundrop Town!")
   

    def town_menu(player):
        print(f"\nDAY {player['day']}")
        print("----- Sundrop Town -----")
        print("(B)uy stuff")
        print("See Player (I)nformation")
        print("See Mine (M)ap")
        print("(E)nter mine")
        print("Sa(V)e game")
        print("(Q)uit to main menu")
        print("------------------------")
        print(f"You start with a backpack that can hold a maximum of {player['backpack_capacity']} pieces of mineral ore.")
        choice = input("Your choice? ").strip().lower()
        return choice

def show_shop_menu(player):
    print("\n----------------------- Shop Menu -------------------------")
    print(f"GP: {player['gp']}")
    if player['pickaxe_level'] == 1:
        print("(P)ickaxe upgrade to level 2 (silver) - Cost: 50 GP")
    elif player['pickaxe_level'] == 2:
        print("(P)ickaxe upgrade to level 3 (gold) - Cost: 150 GP")
    else:
        print("Pickaxe fully upgraded.")

    print(f"(B)ackpack upgrade (+2 capacity) - Cost: 20 GP (Current capacity: {player['backpack_capacity']})")
    print("(L)eave shop")
    print("-----------------------------------------------------------")
    choice = input("Your choice? ").strip().lower()
    return choice

def buy_items(choice, player):
    if choice == 'p':
        if player['pickaxe_level'] == 1:
            cost = 50
            next_level = 2
        elif player['pickaxe_level'] == 2:
            cost = 150
            next_level = 3
        else:
            print("Your pickaxe is already at max level.")
            return player

        if player['gp'] >= cost:
            player['gp'] -= cost
            player['pickaxe_level'] = next_level
            print(f"Congratulations! Pickaxe upgraded to level {next_level}.")
        else:
            print(f"Not enough GP to upgrade pickaxe. You need {cost} GP.")

    elif choice == 'b':
        cost = 20
        if player['gp'] >= cost:
            player['gp'] -= cost
            player['backpack_capacity'] += 2
            print(f"Backpack capacity increased to {player['backpack_capacity']}.")
        else:
            print(f"Not enough GP to upgrade backpack. You need {cost} GP.")

    elif choice == 'l':
        print("Leaving shop.")
    else:
        print("Invalid choice in shop.")

    return player

def player_information(player):
    print("\n----- Player Information -----")
    print(f"Name: {player['name']}")
    print(f"Day: {player['day']}")
    print(f"GP: {player['gp']}")
    print(f"Pickaxe Level: {player['pickaxe_level']}")
    print(f"Backpack Capacity: {player['backpack_capacity']}")
    print(f"Backpack Contents: {player['backpack']}")
    print("------------------------------")

if __name__ == "__main__":
    main()