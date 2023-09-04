# The Terminal Game

# NOTE: THE TERMINAL GAME IS STILL IN ALPHA! EXPECT BUGS AND UNFINESHED/NON PRESENT LEVELS

## What Is The Terminal Game

The terminal game is an RPG bulit with no dependencies in the terminal.

## Installation

### Requirements

- Python 3.8+ (tested only on the most recent Python version)
- Software with .zip support
- An ASCII capable terminal (MacOS/Windows terminal/Most popular linux distros should have this automatically)

### Installation Instructions

First install Python. Consult the [python.org download page](https://python.org/downloads) and follow the instructions for your OS.

Then go to [github.com/micziz/theterminalgame/releases](github.com/micziz/theterminalgame/releases) and download the version you like the most (the latest is recommended).

Download the zip and unzip it. Then open your terminal and cd into your downloads folder.

Default should be:

MacOS and Linux:

```shell
cd ~/Downloads
```

Windows:

```cmd
cd C:\Users\%USERNAME%\Downloads
```

(replace %USERNAME% with the current user)

## How to play

W: Go up
S: Go down
A: Go left
D: Go right

If enemy is below them:

E: Swing sword. Kills enemy and drops 1 coin
Q: Push enemy. Pushes him until the end of the available space

If chest is below the player:

O: Opens the chest. To collect reward walk over it.

## Todo

- [x] Basic movements
- [x] Kill
- [x] Push
- [x] Open
- [x] Collisions
- [x] Title screen
- [ ] Add checks for what actions are possible
- [ ] Save and continue
- [ ] Multiple levels
- [ ] Bosses
- [ ] Story
- [ ] Comments
- [ ] Full manual

## License

License is MIT. More info in the [LICENSE](./LICENSE) file
