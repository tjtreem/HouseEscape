from game_data import rooms

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
                print("the storage room is already open.")
                return

        else:
            print("You can only use the crowbar on the doors to the north and the west.")
            return

    elif item == "kitchen knife" and current_room == "study":
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
        inventory.remove("kitchen knife")

        return "drawer_opened"

              













                                


                              

