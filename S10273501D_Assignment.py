def display_main_menu():
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
    return choice

def start_new_game():
    name = input("Greetings, miner! What is your name? ").strip()
    print(f"Pleased to meet you, {name}. Welcome to Sundrop Town!")
    day = 1
    sundrop_town_menu(day, name)

def sundrop_town_menu(day, name):
    print(f"DAY {day}")
    print("----- Sundrop Town -----")
    print("(B)uy stuff")
    print("See Player (I)nformation")
    print("See Mine (M)ap")
    print("(E)nter mine")
    print("Sa(V)e game")
    print("(Q)uit to main menu")
    print("------------------------")
    choice = input("Your choice? ").strip().lower()
    # Here you can route choices to functions (buy, show info, etc.)
    # For now just placeholder:
    print(f"You chose: {choice.upper()}")

# Main program loop
while True:
    choice = display_main_menu()
    if choice == 'n':
        start_new_game()
    elif choice == 'l':
        print("Loading saved game...")
        # Load game logic goes here
    elif choice == 'q':
        print("Quitting game. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")

