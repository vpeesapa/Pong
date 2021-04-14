# Pong

**Author**: Varun Peesapati

## Objective of Project
The main objective of this project was to development an implementation of the 1972 table tennis-themed classic arcade video game, **Pong**, originally developed by Atari using the `PyGame` SDL from Python.

## Description of Project
1. **main.py**: Script that initializes the game engine and runs the main gameplay loop and its accompanying logic.
2. **paddle.py**: Script that allows `main.py` to create the paddles that are controlled by both players.
3. **ball.py**: Script that allows `main.py` to create the ball that will be hit back and forth by the players.
4. **colors.py**: Script that contains a dictionary containing the RGB values for approximately thirty colors. Is a supplemental script to avoid the tedium of writing RGB values from scratch and instead, simply import this file.

## Organization of Project
```bash
$ tree .
.
├── 8bitOperatorPlus-Regular.ttf
├── ball.py
├── colors.py
├── main.py
├── paddle.py
└── README.md
```

## Usage
```bash
$ python3 main.py
```

Creating an executable:
```bash
$ pyinstaller main.py --onefile
```
The above code creates two new directories, namely `build` and `dist`. `build` contains all the essential scripts needed to build the executable while `dist` contains the executable itself.
**Note**: When the executable is first created, the `dist` directory only contains the executable and no other other file. So, if you have any images or fonts that you are using in your game, be sure to copy them to the `dist` directory for the executable to run without any hiccups

Running the executable:
```bash
$ cd dist
$ ./main
```