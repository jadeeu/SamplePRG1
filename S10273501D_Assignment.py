import random
import sys

# ---------- Player Data Structure ----------
player = {
    "name": "",
    "gp": 0,
    "pickaxe_level": 1,  # 1 = copper, 2 = silver, 3 = gold
    "backpack_capacity": 10,
    "backpack": {"copper": 0, "silver": 0, "gold": 0},
    "portal_position": (7, 1),
    "steps_taken": 0,
    "day": 1
}

# ---------- Intro & Main Menu ----------
def display_intro():
    print("---------------- Welcome to Sundrop Caves! ----------------")
    print("You spent all your money to get the deed to a mine, a small")
    print("backpack, a simple pickaxe and a magical portal stone.")
    print("How quickly can you get the 500 GP you need to retire")
    print("and live happily ever after?")
    print("-----------------------------------------------------------")

def display_main_menu():
    print("--- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
    print("(Q)uit")
    print("------------------")

# ---------- Auto-Sell Ores ----------
def auto_sell_ores():
    total_earned = 0
    sale_prices = {
        "copper": random.randint(1, 3),
        "silver": random.randint(5, 8),
        "gold": random.randint(10, 18)
    }

    for mineral, qty in player["backpack"].items():
        if qty > 0:
            earned = qty * sale_prices[mineral]
            total_earned += earned
            player["backpack"][mineral] = 0

    if total_earned > 0:
        player["gp"] += total_earned
        print(f"You sold your ores for {total_earned} GP!")

# ---------- Shop Menu ----------
def shop_menu():
    while True:
        print("----------------------- Shop Menu -------------------------")
        if player["pickaxe_level"] == 1:
            print("(P)ickaxe upgrade to Level 2 to mine silver ore for 50 GP")
        elif player["pickaxe_level"] == 2:
            print("(P)ickaxe upgrade to Level 3 to mine gold ore for 100 GP")

        next_capacity = player["backpack_capacity"] + 2
        upgrade_cost = player["backpack_capacity"] * 2
        print(f"(B)ackpack upgrade to carry {next_capacity} items for {upgrade_cost} GP")
        print("(L)eave shop")
        print("-----------------------------------------------------------")
        print(f"GP: {player['gp']}")
        print("-----------------------------------------------------------")

        choice = input("Your choice? ").lower()

        if choice == "p":
            if player["pickaxe_level"] == 1 and player["gp"] >= 50:
                player["gp"] -= 50
                player["pickaxe_level"] = 2
                print("Congratulations! You can now mine silver ore!")
            elif player["pickaxe_level"] == 2 and player["gp"] >= 100:
                player["gp"] -= 100
                player["pickaxe_level"] = 3
                print("Congratulations! You can now mine gold ore!")
            else:
                print("Not enough GP or max level reached.")
        elif choice == "b":
            if player["gp"] >= upgrade_cost:
                player["gp"] -= upgrade_cost
                player["backpack_capacity"] = next_capacity
                print(f"Congratulations! You can now carry {next_capacity} items!")
            else:
                print("Not enough GP!")
        elif choice == "l":
            break
        else:
            print("Invalid choice.")

# ---------- Player Information ----------
def show_player_info():
    pickaxe_names = {1: "copper", 2: "silver", 3: "gold"}
    print("----- Player Information -----")
    print(f"Name: {player['name']}")
    print(f"Portal position: {player['portal_position']}")
    print(f"Pickaxe level: {player['pickaxe_level']} ({pickaxe_names[player['pickaxe_level']]})")
    print("------------------------------")
    load = sum(player["backpack"].values())
    print(f"Load: {load} / {player['backpack_capacity']}")
    print("------------------------------")
    print(f"GP: {player['gp']}")
    print(f"Steps taken: {player['steps_taken']}")
    print(f"Day: {player['day']}")
    print("------------------------------")

# ---------- Town Menu ----------
def town_menu():
    auto_sell_ores()  # Sell ores automatically when entering town

    while True:
        print(f"DAY {player['day']}")
        print("----- Sundrop Town -----")
        print("(B)uy stuff")
        print("See Player (I)nformation")
        print("See Mine (M)ap")
        print("(E)nter mine")
        print("Sa(V)e game")
        print("(Q)uit to main menu")
        print("------------------------")

        choice = input("Your choice? ").lower()

        if choice == "b":
            shop_menu()
        elif choice == "i":
            show_player_info()
        elif choice == "q":
            break
        else:
            print(f"Option '{choice}' not yet implemented.")

# ---------- Game Start ----------
def start_new_game():
    player["name"] = input("Greetings, miner! What is your name? ")
    player["gp"] = 0
    player["pickaxe_level"] = 1
    player["backpack_capacity"] = 10
    player["backpack"] = {"copper": 0, "silver": 0, "gold": 0}
    player["steps_taken"] = 0
    player["day"] = 1
    print(f"Pleased to meet you, {player['name']}. Welcome to Sundrop Town!")
    town_menu()

def load_game():
    # Placeholder for loading logic
    print("Loading saved game...")
    # TODO: Load from file
    town_menu()

def quit_game():
    print("Thanks for playing Sundrop Caves. Goodbye!")
    sys.exit()

# ---------- Main Loop ----------
def main():
    display_intro()
    while True:
        display_main_menu()
        choice = input("Your choice? ").lower()

        if choice == "n":
            start_new_game()
        elif choice == "l":
            load_game()
        elif choice == "q":
            quit_game()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
