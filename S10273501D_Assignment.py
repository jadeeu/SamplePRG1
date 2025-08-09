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
            discovered = player.get("discovered")
            if not discovered:
                discovered = [[False]*mine_width for _ in range(mine_height)]
            print_town_map(mine_map, discovered, player)

        elif choice == 'e':
            won = enter_mine(player)
            if won:
                print("Returning to main menu...")
                break

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
    list("T CCCCC SS GGG"),
    list(" CCCCC SSSS   "),
    list("GGG           "),
    list(" CCCC SSSS GGG"),
    list(" SSSSS CCC    "),
    list(" CC S CCCC    "),
    list("CCCCCCCCC CCCCC"),
    list("CCCCCCCC G CCCC"),
    list(" CCCCC GG SS  "),
    list(" CCCCC GGG    "),
    list("SSSSSS        "),
    list(" CCC GGG      "),
    list("SSSGGG        ")
]

mine_height = len(mine_map)
mine_width = max(len(row) for row in mine_map)

# Pad all rows to same width for safety
for i in range(mine_height):
    if len(mine_map[i]) < mine_width:
        mine_map[i] += [' '] * (mine_width - len(mine_map[i]))

def initialize_discovered(width, height, player_x, player_y):
    discovered = [[False] * width for _ in range(height)]
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
    print("+" + "-" * mine_width + "+")
    for y in range(mine_height):
        row = "|"
        for x in range(mine_width):
            if x == player_x and y == player_y:
                row += "M"
            elif discovered[y][x]:
                row += mine_map[y][x]
            else:
                row += "?"
        row += "|"
        print(row)
    print("+" + "-" * mine_width + "+")

def print_town_map(mine_map, discovered, player):
    portal_x, portal_y = player.get("portal_position", (7, 1))
    player_x, player_y = 0, 0  # Player is always at top-left in town

    print("+" + "-" * mine_width + "+")
    for y in range(mine_height):
        row = "|"
        for x in range(mine_width):
            if x == player_x and y == player_y:
                row += "M"
            elif x == portal_x and y == portal_y:
                row += "P"
            elif discovered[y][x]:
                row += mine_map[y][x]
            else:
                row += "?"
        row += "|"
        print(row)
    print("+" + "-" * mine_width + "+")

def enter_mine(player):
    # Start at portal position or (0,0) if missing
    player_x, player_y = player.get("portal_position", (0,0))
    # Use saved discovered map or initialize
    discovered = player.get("discovered")
    if not discovered:
        discovered = initialize_discovered(mine_width, mine_height, player_x, player_y)
    player["mine_steps"] = 0
    player["discovered"] = discovered

    while True:
        print_full_map(mine_map, discovered, player_x, player_y)
        print(f"Steps in mine: {player['mine_steps']} / 20")
        print("\nMove with WASD keys, (Q)uit mine:")
        move = input("Your move? ").strip().lower()

        if move == 'q':
            print("Exiting mine...")
            break

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

        if 0 <= new_x < mine_width and 0 <= new_y < mine_height:
            player_x, player_y = new_x, new_y
            update_discovered(discovered, player_x, player_y)
            player["steps"] += 1
            player["mine_steps"] += 1

            # Try to collect ore if any, if backpack capacity allows
            tile = mine_map[player_y][player_x]
            ore_types = {"C": "copper", "S": "silver", "G": "gold"}
            ore = ore_types.get(tile.upper())
            if ore:
                total_ore = sum(player["backpack"].values())
                if total_ore < player["backpack_capacity"]:
                    player["backpack"][ore] += 1
                    print(f"You mined 1 {ore} ore!")
                    mine_map[player_y][player_x] = ' '
                else:
                    print("Your backpack is full! Sell some ores before mining more.")
            else:
                print("Nothing to mine here.")

        else:
            print("You cannot move outside the mine!")
            continue

def return_to_town(player, discovered, player_x, player_y):
    print("\nReturning to town...")

    # Randomised prices each return
    import random
    prices = {
        "copper": random.randint(1, 3),
        "silver": random.randint(5, 8),
        "gold" : random.randint(10, 18)
    }

    # Sell ores
    total_value = 0
    for ore, qty in player["backpack"].items():
        if qty > 0:
            ore_value = prices[ore] * qty
            total_value += ore_value
            print(f" Sold {qty} {ore} for {ore_value} GP ({prices[ore]} GP each)")
            player["backpack"][ore] = 0

    if total_value > 0:
        print(f" Total earned: {total_value} GP!")
        player["gp"] += total_value
    else:
        print("You had nothing to sell.")

    # Day passes
    player["day"] += 1
    print(f" It's now Day {player['day']}.")

    # Reset mine state
    player["mine_steps"] = 0
    player["portal_position"] = (player_x, player_y)
    player["discovered"] = discovered

    # Win condition
    if player["gp"] >= 500:
        print("-------------------------------------------------------------")
        print(f"Woo-hoo! Well done, {player['name']}, you have {player['gp']} GP!")
        print("You now have enough to retire and play video games every day.")
        print(f"And it only took you {player['day']} days and {player['steps']} steps! You win!")
        print("-------------------------------------------------------------")
        return True  # game won
    return False  # keep playing


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
