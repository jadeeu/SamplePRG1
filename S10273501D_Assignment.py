import json
import os

def display_intro_and_main_menu():
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
        "backpack": {"copper": 0, "silver": 0, "gold": 0},
        "portal_position": (7, 1),
        "steps": 0
    }
    print(f"Pleased to meet you, {name}. Welcome to Sundrop Town!")
    town_menu(player)

def town_menu(player):
    while True:
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

        if choice == 'b':
            while True:
                shop_choice = show_shop_menu(player)
                if shop_choice == 'l':
                    break
                player = buy_items(shop_choice, player)

        elif choice == 'i':
            player_information(player)

        elif choice == 'm':
            print("\nMine map will be displayed here. (Coming soon...)")

        elif choice == 'e':
            print("\nEntering the mine... (Coming soon...)")

        elif choice == 'v':
            save_game(player)

        elif choice == 'q':
            print("\nReturning to main menu...")
            break

        else:
            print("Invalid choice. Try again.")

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
    pickaxe_names = {1: "copper", 2: "silver", 3: "gold"}
    print(f"Pickaxe Level: {player['pickaxe_level']} ({pickaxe_names[player['pickaxe_level']]})")
    print(f"Backpack Capacity: {player['backpack_capacity']}")
    print(f"Backpack Contents: {player['backpack']}")
    print(f"Portal Position: {player['portal_position']}")
    print(f"Steps Taken: {player['steps']}")
    print("------------------------------")

mine_map = [
    list("  C ???????????????????"),
    list(" CP ???????????????????"),
    list("????CCCC ???????????????????"),
    list("??????????????????????????????"),
    list("??????????????????????????????"),
    list("??????????????????????????????"),
    list("??????????????????????????????"),
    list("??????????????????????????????"),
    list("??????????????????????????????"),
    list("??????????????????????????????"),
]

mine_width = len(mine_map[0])
mine_height = len(mine_map)

# Your functions you gave me:

def initialize_discovered(width, height, player_x, player_y):
    discovered = [[False for _ in range(width)] for _ in range(height)]
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            nx, ny = player_x + dx, player_y + dy
            if 0 <= nx < width and 0 <= ny < height:
                discovered[ny][nx] = True
    return discovered

def update_discovered(discovered, player_x, player_y):
    height = len(discovered)
    width = len(discovered[0])
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            nx, ny = player_x + dx, player_y + dy
            if 0 <= nx < width and 0 <= ny < height:
                discovered[ny][nx] = True

def print_full_map(mine_map, discovered, player_x, player_y):
    height = len(mine_map)
    width = len(mine_map[0])
    print("+" + "-" * width + "+")
    for y in range(height):
        row = "|"
        for x in range(width):
            if x == player_x and y == player_y:
                row += "M"
            elif (x, y) == (7, 1):  # portal position, hardcoded or from player.portal_position
                row += "P"
            elif discovered[y][x]:
                row += mine_map[y][x]
            else:
                row += "?"
        row += "|"
        print(row)
    print("+" + "-" * width + "+")

def print_viewport(mine_map, player_x, player_y):
    height = len(mine_map)
    width = len(mine_map[0])
    print("+---+")
    for dy in range(-1, 2):
        row = "|"
        for dx in range(-1, 2):
            nx, ny = player_x + dx, player_y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if nx == player_x and ny == player_y:
                    row += "M"
                else:
                    row += mine_map[ny][nx]
            else:
                row += " "
        row += "|"
        print(row)
    print("+---+")

def enter_mine(player):
    # Starting player position inside mine (example)
    player_x, player_y = 0, 0
    discovered = initialize_discovered(mine_width, mine_height, player_x, player_y)

    while True:
        print_full_map(mine_map, discovered, player_x, player_y)
        print("\nMove with WASD keys, (Q)uit mine:")
        move = input("Your move? ").strip().lower()

        if move == 'q':
            print("Exiting mine...")
            break

        # Calculate new position
        dx, dy = 0, 0
        if move == 'w':
            dy = -1
        elif move == 's':
            dy = 1
        elif move == 'a':
            dx = -1
        elif move == 'd':
            dx = 1
        else:
            print("Invalid move. Use W,A,S,D or Q.")
            continue

        new_x = player_x + dx
        new_y = player_y + dy

        # Check bounds
        if 0 <= new_x < mine_width and 0 <= new_y < mine_height:
            player_x, player_y = new_x, new_y
            update_discovered(discovered, player_x, player_y)
            player["steps"] += 1  # track steps taken in the mine
        else:
            print("You cannot move outside the mine!")

# Modify your town_menu to call enter_mine when player selects 'e'

def town_menu(player):
    while True:
        print(f"\nDAY {player['day']}")
        print("----- Sundrop Town -----")
        print("(B)uy stuff")
        print("See Player (I)nformation")
        print("See Mine (M)ap")
        print("(E)nter mine")
        print("Sa(V)e game")
        print("(Q)uit to main menu")
        print("------------------------")
        choice = input("Your choice? ").strip().lower()

        if choice == 'b':
            while True:
                shop_choice = show_shop_menu(player)
                if shop_choice == 'l':
                    break
                player = buy_items(shop_choice, player)

        elif choice == 'i':
            player_information(player)

        elif choice == 'm':
            # Show full map with fog and discovery
            # For simplicity, just call print_full_map with all tiles discovered except fog for unexplored
            # You can store discovered grid as player state or just show full map here
            # Let's assume we show full map with all tiles visible in town:
            discovered_all = [[True]*mine_width for _ in range(mine_height)]
            print_full_map(mine_map, discovered_all, 0, 0)  # Player is at 0,0 in town map view

        elif choice == 'e':
            enter_mine(player)

        elif choice == 'v':
            save_game(player)

        elif choice == 'q':
            print("\nReturning to main menu...")
            break

        else:
            print("Invalid choice. Try again.")

def main():
    while True:
        display_intro_and_main_menu()
        choice = input("Enter choice: ").strip().lower()
        if choice == 'n':
            new_game()
        elif choice == 'l':
            player = load_game()
            if player:
                town_menu(player)
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
