


rooms = {
    "basement": {
        "description": (
            "You awaken in a dark area with no memory of how you got there. The only light is coming "
            "from a dirty, small window high up on a featureless wall above you. Looking around, your "
            "eyes adjusting to the gloom, you realize you seem to be in a basement of some sort. It's "
            "cold and damp with the smell of rot and old metal. As you try to get your bearings, you "
            "hear the creak of floorboards above you."
        ),
        "reentry": (
            "The chill greets you again as you return to the basement. Nothing *seems* to have moved...right?"
        ),
        "exits": {"north": "storage_room", "west": "stairwell"},
        "items": ["crowbar"],
        "locked": False
    },

    "storage_room": {
        "description": (
            "The storage room is cluttered with broken furniture, moldy boxes filled with papers and "
            "photographs, and crates that seem to hold an array of assorted items, some of which look "
            "suspiciously like bones. You notice a small crawlspace closed off with a heavy padlock " 
            "behind an old armoire. Try as you might, you can't seem to reach it without shifting the "
            "pile of clutter, which starts making noise that could possibly be heard. The air feels "
            "oppressive, and the padlocked door seems to move slightly... or maybe it's your imagination?"
        ),
        "reentry": (
            "The musty air in the storage room hasn't changed, but...there's a scratching noise "
            "definitely coming from behind that locked crawlspace."
        ),
        "exits": {"south": "basement"},
        "items": ["rusty_key"],
        "locked": True # Requires crowbar for storage room door

    },

    "stairwell": {
        "description": (
            "The narrow stairwell leads up into the darkness, with only the first few old wooden stairs "
            "illuminated by the dim window light. A small, dusty light suspended from the ceiling at the "
            "top of the stairs shows the silhouette of a wooden door. Where this door may lead to is "
            "anyone's guess, but it seems to be the only way forward."
        ),
        "reentry": (
            "The narrow stairway yawns downward like a hungry throat. You descend slowly, listening..."
        ),
        "exits": {"up": "kitchen", "down": "basement"},
        "items": [],
        "locked": False
    },
    
    "kitchen": {
        "description": (
            "You enter a dusty and long-unused kitchen area. Looking around, you see cabinets with their "
            "doors either standing wide open or, in some cases, hanging from broken hinges or missing "
            "entirely. A fine layer of dust seems to cover everything there...everything except a large "
            "kitchen knife lying on the counter on top of reddish stains that you hope are from spilled "
            "wine. You see wan sunlight streaming in from the dirty windows above the kitchen sink, which "
            "is full of old, dented pots festooned with mold. A single trail of large footprints on the kitchen floor"
            "leads away from the basement door towards the counter and then off to the south into an adjoining "
            "room..."
        ),
        "reentry": (
            "The kitchen is silent once more. That knife stain looks suspiciously fresh. Are those more footprints "
            "moving towards the basement door? Or are they yours?"
        ),
        "exits": {"south": "dining_room"},
        "items": ["kitchen_knife"],
        "locked": True # Requires rusty key
    },

    "dining_room": {
        "description": (
            "The dining room is a strange scene: the table is set and plates are covered with food which "
            "seem to be infested with creatures that look like maggots. Ornate crystal goblets sit, dusty and "
            "untouched, containing a type of red liquid which is layered with some kind of...fungus? "
            "The blue curtains on the windows are tattered and torn, and fading sunlight streams in on "
            "the table, shining almost like spotlights to highlight the disturbing state of the meal "
            "and causing you to shudder in revulsion. Two of the dining room chairs are overturned and "
            "there are more of those reddish stains under the layer of dust on the floor near them. The "
            "ghostly line of footprints leading here from the kitchen ends and disappears near the "
            "table.  An arched opening leads out of the ghastly dining area and you can vaguely see a "
            "large door that might open to the outside world and hopefully, safety. You can faintly hear "
            "the creaking of more floorboards coming from somewhere above on another floor of the house."
        ),
        "reentry": (
            "Back in the dining room, the rotting meal still festers under the dying rays of the fading sun. The "
            "shadows are growing longer..."
        ),
        "exits": {"south": "foyer", "north": "kitchen"},
        "items": [],
        "locked": False
    },

    "foyer": {
        "description": (
            "The foyer is very wide, and it is strewn with what may have once been comfortable chairs, "
            "but are now ripped and split open by jagged slashes that have exposed their innards, "
            "indicating a level of violence that contrasts with the deathly quiet of the house. The "
            "doors you saw from the dining room are on your right. Straight ahead you see the entrance "
            "to a library or study of some kind. To your left is a short, wide hallway leading to "
            "another stairwell that rises into the shadows. Moving slowly and carefully to avoid making "
            "noise, you approach the large double doors and through the stained glass windows you can "
            "see trees blowing in the wind being illuminated by the fading sunlight as nightfall "
            "approaches. This is definitely the way out! With excitement, you grab the ornate door " 
            "handle, freedom only moments away...but it's locked tight."
        ),
        "reentry": (
            "You step back into the foyer. The lengthening shadows make the shredded furniture look like teeth. "
            "You hear shuffling footsteps at the top of the stairs. Someone - or *something* - is beginning to plod "
            "heavily down towards you."
            ),
        "exits": {
            "north": "dining_room",
            "south": "study",
            "west": "outside",
            "east": "hallway",
            "up": "stairwell"
            },
        "items": [],
        "locked": False
    },

    "study": {
        "description": (
            "You enter a spacious area that best resembles a study of some kind. The walls are lined "
            "with bookcases, all of them dusty and cobwebbed, with row upon row of books sitting snugly "
            "on shelves. A dampness permeates the air, and many of the books seem to be covered with "
            "mold, evidence that this study has remained unused for some time. On the far side of the "
            "room is a large desk, with a wide-backed chair behind it and mullioned windows along the "
            "far wall. The sunlight seems to have faded even more as you survey the room and the shadows "
            "looming in the corners deepen into darkness, giving the study a sinister look. You hear "
            "faint movement above you, as someone, or something, moves through the unseen rooms on the "
            "upper floors. If only you can find the key to the front door..."
        ),
        "reentry": (
            "Back in the study, the books seem almost to stare at you accusingly, as if you're the cause of "
            "everything that's wrong here."
        ),
        "exits": {"north": "foyer"},
        "items": [],
        "locked": False
    },
    
    "outside": {
        "description": (
            "You step outside into the fading light of dusk, slamming the doors behind you and starting "
            "down the stone steps of the front porch. Twisted vines of ivy grow haphazardly along and "
            "above the porch and the bannisters of the steps as you try to put distance between you and "
            "that house of horrors. Cool air rushes past you as you move quickly down the stone path, " 
            "each step leading you further and further away from your captor. As you approach the safety "
            "of the adjoining street, you bend over, placing your hands on your knees in abject relief "
            "as you take a deep breath - the first one that seems real in hours. The cool air rustles "
            "the tops of the trees as the sun finally dips below the horizon behind the imposing house, "
            "and night falls. The oppressive weight you've carried through the house begins to lift. You "
            "made it. *You're safe*.\n\n"
        ),
        "reentry": (
            "Stepping back outside, something feels different. A sense of...wrongness...fills the air. Freedom "
            "isn't here...not yet."
        ),
        "exits": {},
        "items": [],
        "locked": True
    },
}
            


 














































