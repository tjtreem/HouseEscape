# Get Out!

A text-based psychological horror escape room.  
Written in Python. Played in the Linux CLI. Best experienced in the dark.

---

## How to Play

Explore a rotting house. Collect strange items.  
Avoid whatever trapped you inside.

**Commands**
- `go [direction]` — Move between rooms (e.g., `go north`)
- `take [item]` / `drop [item]` — Manage inventory
- `use [item]` — Interact with the environment
- `inventory` or `i` — View what you're carrying
- `inspect [item]` — Look closer (planned)
- `help` — Show available commands
- `quit` — Exit the game

---

## Sound Design

Background ambience loops per room.  
Sound effects trigger on item interaction.  
All audio handled via `ffplay`.

---

## Project Structure


<pre> ``` Get_Out!/ ├── main.py # Game entry point ├── game_data.py # Rooms, descriptions, exits, item placements ├── item_data.py # Item descriptions and properties ├── player.py # Player state and inventory logic ├── game_logic.py # Command handling (use, take, etc.) ├── utils.py # Helper functions (e.g., slow_print, clear_screen) ├── sounds/ # .wav files for ambient and SFX └── README.md # You're reading it! ``` </pre>
---

## Linux Compatibility

Designed to run inside **WSL** for full CLI-based immersion.  
Tested with `Python 3.12+` and `ffplay` for Windows via WSL.

---

## Planned Features

- Persistent room ambience (looped)
- Unique sound effects per item
- `inspect` command for environmental lore
- Timed/triggered scare events
- Multiple endings based on choices

---

## License

For educational/personal use only.  
All sounds are sourced manually by the author or are placeholders.










