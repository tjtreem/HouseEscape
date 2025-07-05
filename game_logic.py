from game_data import rooms
from item_data import item_descriptions


def use_item(item, current_room, inventory):
    if item == "crowbar" and current_room == "basement":
        direction = input("Use crowbar on which door? (north or west): ").strip().lower()

        if direction == "west":
            confirm = input(
                    "This door is inordinately solid. There's no way to pry it open quietly. "
                    "Proceed? (yes/no): "
                    ).strip().lower()

            if confirm == "yes":
                print(
                    "You jam the crowbar into the door frame and pry it as hard as you can... "
                    "With a loud screetch of metal and wood, the door flys open..."
                    "You see a dimly lit kitchen area, but then a shadow fills the doorway... "
                    "A huge, hulking presence grabs you roughly with one hand and you feel "
                    "the searing pain of a knife plunged into your chest...\n\n"
                    "Your vision fades to black...\n\n"
                    "*END*"
                )
                return "bad_ending"
            else:
                print("You hesitate and back slowly down the stairs. The door remains shut.")
                return

        elif direction == "north":
            if rooms["storage_room"]["locked"]:
                rooms["storage_room"]["locked"] = False
                print(
                        "You wedge the crowbar between the padlocked door and the frame. With effort, "
                    "the hasp of the lock gives way and the door creaks open quietly, revealing "
                    "what seems to be a cluttered storage room."
                )
                return "unlocked_storage"

            else:
                print("The storage room is already open.")
                return

        else:
            print("You can only use the crowbar on the doors to the north and the west.")
            return

    elif item == "kitchen_knife" and current_room == "study":
        if "front_door_key" in inventory or "front_door_key" in rooms["study"]["items"]:
            print("The drawer is already pried open, and the key is visible.")
            return
        
        print("You circle around the desk and roll the chair out of the way. There are several "
              "drawers in the desk, most of which are either empty or contain stacks of papers "
              "covered in mold. The center drawer is locked tightly. You wedge the kitchen knife into "
              "the small gap of the drawer and apply steady pressure. The blade bends-then snaps with "
              "a metallic *twang*-but the drawer pops open, revealing a large brass key. There is "
              "only one door that would require a key of this size.\n\n"
              "You take the front door key and drop the broken knife handle to the floor."
              )

        # Add key to inventory or room
        inventory.append("front_door_key")

        # Remove knife from inventory
        inventory.remove("kitchen_knife")

        return "drawer_opened"

    elif item == "rusty_key" and current_room == "stairwell":
        if rooms["kitchen"]["locked"]:
            rooms["kitchen"]["locked"] = False
            print("You slide the rusty key into the old lock with some effort. You turn the key, and "
                  "for a heart-stopping moment the key doesn't turn. Holding your breath, you turn it "
                  "harder, praying that it won't break. Finally, with a reluctant *CLICK*, it turns and "
                  "the door slowly creaks inwards and leads you into the kitchen area. Looking around "
                  "fearfully, you attempt to remove the key from the lock but the rust holds it fast."
            )

            inventory.remove("rusty_key")

            return "kitchen_unlocked"

        else:
            print("The stairwell door is already unlocked.")
            return

    elif item == "front_door_key" and current_room == "foyer":
        if rooms["outside"]["locked"]:
            rooms["outside"]["locked"] = False
            print("You fit the large brass key into the ornate lock. It rotates smoothly and turns with "
                  "a heavy *CLUNK*.\n"
                  "The double doors swing open slightly. Finally! The way out!!"
            )
            return "door_unlocked"

        else:
            print("The door is already unlocked.")
            return

    else:
        print("You can't use that here.")
        return




def handle_inventory_command(command, current_room, inventory, rooms):
    words = command.strip().lower().split()

    if command in ["inventory", "i"]:
        if not inventory:
            print("You are not carrying anything.")
        else:
            print("You're carrying: ")
            for item in inventory:
                print(f" - {item.replace('_', ' ')}")
        return

    if words[0] == "take" and len(words) > 1:
        item = '_'.join(words[1:])
        if item in rooms[current_room]["items"]:
            inventory.append(item)
            rooms[current_room]["items"].remove(item)

            # Print the item and the item description, if available
            print(f"You pick up the {item.replace('_', ' ')}. {item_descriptions[item]}")
            
        else:
            print(f"There is no {item.replace('_', ' ')} here to take.")
        return

    if words[0] == "drop" and len(words) > 1:
        item = ('_').join(words[1:])
        if item in inventory:
            inventory.remove(item)
            rooms[current_room]["items"].append(item)
            print(f"You drop the {item.replace('_', ' ')}.")
        else:
            print(f"You're not carrying a {item.replace('_', ' ')}.")
        return

    print("I don't understand that inventory command.")























