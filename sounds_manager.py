import subprocess
import os



SOUND_DIR = os.path.join(os.path.dirname(__file__), "sounds")

def play_sound(filename):
    sound_path = os.path.join(SOUND_DIR, filename)

    if not os.path.exists(sound_path):
        print(f"[Sound Error] File not found: {sound_path}")
        return

    subprocess.run(
        ["ffplay", "-nodisp", "-autoexit", sound_path]
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def play_room_entry(room_name):
    room_sounds = {
        "basement": "basement_ambience.mp3",
        "storage_room": "creak_door.mp3",
        "stairwell": "footsteps_up.mp3",
        "kitchen": "knife_pickup.mp3",
        "dining_room": "flies_buzzing.mp3",
        "foyer": "door_locked.mp3",
        "study": "pages_rustle.mp3";
        "outside": "wind_gust.mp3",
    }

    if room_name in room_sounds:
        play_sound(room_sounds[room_name])


def play_item_pickup(item_name):
    item_sounds = {
        "crowbar": "metal_pickup.mp3",
        "rusty_key": "key_clink.mp3",
        "kitchen_knife": "knife_scrape.mp3",
        "front_door_key": "key_ominous.mp3",
    }

    if item_name in item_sounds:
        play_sound(item_sounds[item_name])


def play_event(event):
    event_sounds = {
        "bad_ending": "stab_scream.mp3",
        "door_unlock": "door_unlock.mp3",
        "door_open": "door_open.mp3",
        "drawer_break": "drawer_break.mp3",
    }

    if event in event_sounds:
        play_sound(event_sounds[event])






















