# The Terminal Game

PLEASE NOTE: The terminal game is still in development. Bugs will be present. We are working as hard as we can to give you a finshed product, but it might take some time.

## What Is The Terminal Game

The terminal game is an RPG built with ZERO dependencies that you can play completely in the terminal!

## Installation

### Requirements

- Python 3.8+ (tested only on the most recent Python version)
- An ASCII capable terminal (MacOS/Windows/Most popular linux distros should have this automatically)

If you plan on downloading a stable release (recommended):

- Software with .zip support

If you plan to use the main branch (may be unstable):

- A recent version of git

### Installation Instructions

First install Python. Consult the [python.org download page](https://python.org/downloads) and follow the instructions for your OS.

Stable release (recommended): 

Go to [github.com/micziz/theterminalgame/releases](github.com/micziz/theterminalgame/releases) and download the version you like the most (the latest is recommended).

Download the zip and unzip it. Then open your terminal and cd into the game folder.

Default should be:

MacOS and Linux:

```shell
cd ~/Downloads/theterminalgame-(version)
```

Windows:

```cmd
cd C:\Users\%USERNAME%\Downloads\theterminalgame-(version)
```

(replace %USERNAME% with the current user)
(replace (version) with the version you downloaded)

Main branch:

Copy this command:

```sh
git clone https://github.com/micziz/theterminalgame.git
```

Cd into it:

```sh
cd theterminalgame
```

Now just run python!

Linux And Windows:

```shell
python main.py
```

MacOS:

```shell
python3 main.py
```

## How to play

W: Go up
S: Go down
A: Go left
D: Go right
Z: Save

If an enemy is below you:

E: Swing sword. Kills enemy and drops 1 coin
Q: Push enemy. Pushes him until the end of the available space

If a chest is below you:

O: Opens the chest. To collect reward walk over it.

## Todo

- [x] Basic movements
- [x] Kill
- [x] Push
- [x] Open
- [x] Collisions
- [x] Title screen
- [x] Add checks for what actions are possible
- [x] Multiple levels
- [x] Save and continue
- [ ] How to play in the title screen
- [ ] Bosses
- [ ] Story
- [ ] Design Levels
- [ ] Comments
- [ ] Full manual

## License

License is MIT. More info in the [LICENSE](./LICENSE) file
