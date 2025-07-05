from game_data import rooms
from player import Player
from game_logic import use_item, handle_inventory_command
from utils import clear_screen, slow_print
import time
import os




def title_screen():
    clear_screen()
    slow_print("                                    ...a cold draft on your neck...", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    slow_print("                                    ...the smell of rot in the walls...", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    slow_print("                                    ...a memory you can't quite reach...", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    slow_print("                                    ...the creak of an old floorboard...", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    slow_print("                                                ...you are not...", delay=0.05)
    time.sleep(2.0)
    slow_print("                                                    ...alone...", delay=0.05)
    time.sleep(2.0)
    clear_screen()
    slow_print("                                                 ...wake up...", delay=0.05)
    time.sleep(2.0)
    clear_screen()
    slow_print("\n\n                                                [ HOUSE ESCAPE ]", delay=0.08)
    slow_print("                                A text-based psychological horror escape experience.\n", delay=0.08)
    input(">>> Press ENTER to begin...")


def end_scene():
    time.sleep(2.0)
    clear_screen(),
    slow_print("                        You take that last step towards safety and freedom...\n\n", delay=0.05),
    time.sleep(2.0),
    clear_screen(),
    slow_print("                    ...and a cold hand clamps down on your shoulder from behind...\n\n", delay=0.05),
    time.sleep(2.0),
    clear_screen(),
    slow_print("                        ...the cold sinks in as you're dragged backwards...\n\n", delay=0.05),
    time.sleep(2.0),
    clear_screen(),
    slow_print("                    ...your last coherent thought is lost in the void as your mind goes blank...\n\n", delay=0.05),
    time.sleep(2.0),
    clear_screen(),
    slow_print("                            ...you never even hear the doors close behind you...\n\n", delay=0.05),
    time.sleep(2.0),
    clear_screen(),
    slow_print("                                            THE END...or is it??\n\n", delay=0.10)
    time.sleep(1.0)
    slow_print("                                            Thanks for playing!", delay=0.05)
    



def show_room(room_name, player):
    room = rooms[room_name]
    clear_screen()
    print(f"                        \n=== {room_name.replace('_', ' ').title()} ===\n")


    if room_name not in player.visited_rooms:
        slow_print(room["description"], delay=0.03)
        player.visited_rooms.add(room_name)
    else:
        if "reentry" in room:
            slow_print(room["reentry"], delay=0.03)
        else:
            print("You're back in the " + room_name.replace('_', ' ') + ".")

    
    if room["items"]:
        print(f"Looking around, you see:")
        for item in room["items"]:
            print(f" - {item.replace('_', ' ')}")




def main():
    player = Player(starting_room="basement")

    
    # Show the initial room description
    show_room(player.current_room, player)

    while True:
        command = input("\n> ").strip().lower()

        if command in ["quit", "exit"]:
            print("Thanks for playing. Goodbye!")
            break

        elif command in ["help", "?"]:
            print("Available commands:")
            print("- go [direction] (e.g., go north)")
            print("- take [item]")
            print("- drop [item]")
            print("- use [item]")
            print("- inventory or i")
            print("- quit or exit")
            continue

        elif command.startswith("go "):
            direction = command.split()[1]
            current = rooms[player.current_room]

            if direction in current["exits"]:
                next_room = current["exits"][direction]

                # Check if the room is locked
                if rooms[next_room]["locked"]:
                    print("The door is locked.")
                else:
                    player.current_room = next_room
                    show_room(player.current_room, player)

                    # Check for bad ending trigger
                    if player.current_room == "outside":
                        print("\n\nThanks for playing!")
                        break
            else:
                print("You can't go that way.")
            continue

        elif command.startswith("use "):
            item = command[4:].replace(" ", "_")
            if item in player.inventory:
                result = use_item(item, player.current_room, player.inventory)
                if result == "bad_ending" and not end_scene():
                    print("\n\nThanks for playing.")
                    break
            else:
                print(f"You're not carrying a {item.replace('_', ' ')}.")
            continue

        elif command.startswith("take ") or command.startswith("drop ") or command in ["inventory", "i"]:
            handle_inventory_command(command, player.current_room, player.inventory, rooms)
            continue

        else:
            print("I don't understand that command.")




if __name__ == "__main__":
    title_screen()
    main()
    end_scene()

