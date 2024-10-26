# Mood Swings Game 🎮🎭

**Mood Swings Game** is an engaging and visually interactive 2D game built using Python’s `turtle` graphics library. In this game, players control a character or “blob” to collect falling "moods," represented by colored balls. Each color corresponds to a different emotional state, impacting the player’s overall emotional balance. The goal is to keep mood levels balanced and survive as long as possible.

## Table of Contents

- [Installation](#installation)
- [Game Description](#game-description)
- [Gameplay Mechanics](#gameplay-mechanics)
- [Features](#features)
- [How to Play](#how-to-play)
- [Code Overview](#code-overview)
  - [1. `Moods_Fall` Class](#1-moods_fall-class)
  - [2. `main` Function](#2-main-function)
  - [3. Helper Functions](#3-helper-functions)
- [License](#license)

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/LejhandG/mood-swings-game.git
    cd mood-swings-game
    ```

2. **Install Dependencies**:
    Ensure you have Python installed. This game also requires the `turtle` and `random` modules (both are included in the Python Standard Library).
    
3. **Game Assets**:
    - Place the following image files in the project directory or set paths accordingly in the code:
        - `background.gif`
        - `sad_emoji.gif`
        - `neutral_emoji.gif`
        - `happy_emoji.gif`
  
4. **Run the Game**:
    ```bash
    python main.py
    ```

---

## Game Description

The **Mood Swings Game** challenges players to collect falling mood "balls" while maintaining emotional balance. Each mood impacts the player’s emotional meter based on its color:
   - **Red**: Represents anger
   - **Blue**: Represents sadness
   - **Yellow**: Represents happiness

If any negative mood level crosses a certain threshold, the game ends. The player wins if they maintain emotional stability until the timer runs out.

---

## Gameplay Mechanics

- **Mood Levels**: The game tracks the player's mood levels using a dynamic mood meter. If a mood level crosses the threshold, the game is over.
- **Movement**: The player can move the blob left and right to catch falling moods.
- **Mood Impact**:
    - Red (Angry) and Blue (Sad) moods increase their respective levels.
    - Yellow (Happy) mood increases happiness and decreases anger/sadness slightly.

## Features

- **Dynamic Mood Meter**: Displays mood levels with color-coded bars.
- **Score and Timer Display**: Updates every second, showing time left and current score.
- **Game Over Conditions**: The game ends if anger or sadness reaches 80% or if the timer runs out.
- **Mood-based Blob Appearance**: The blob changes appearance based on the dominant mood.

---

## How to Play

1. **Controls**:
   - Press **'A'** to move left
   - Press **'D'** to move right

2. **Objective**:
   - Catch yellow moods to increase happiness while balancing negative emotions.
   - Avoid letting anger or sadness reach 80%.

3. **Winning Condition**:
   - Survive the full game time without letting negative emotions exceed 80%.

---

## Code Overview

### 1. `Moods_Fall` Class

This is the core class managing mood generation, movement, collision detection, mood levels, score, and the timer.

- **Attributes**:
    - `all_moods`: List storing each falling mood.
    - `mood_levels`: Tracks current levels for each mood (`angry`, `sad`, `happy`).
    - `move_speed`: Determines how fast moods fall.
    - `time_left`: Timer set for 60 seconds.

- **Methods**:
    - `setup_mood_meter()`: Initializes and places the mood meter on screen.
    - `setup_displays()`: Sets up score and timer displays.
    - `create_moods()`: Randomly creates a new falling mood.
    - `move_moods()`: Moves moods downward and removes them if out of screen.
    - `handle_collision(mood, blob)`: Updates mood levels, score, and blob appearance when the blob catches a mood.
    - `update_timer()`: Updates game timer and checks for timeout.
    - `check_game_over()`: Ends the game if any negative mood level reaches 80%.

### 2. `main` Function

The `main()` function initializes the screen, sets up the blob, listens for key presses, and contains the game loop.

- **Screen Setup**: Loads game assets and sets up the background.
- **Blob Setup**: Initializes the blob as the player-controlled character, setting the default shape to `happy_emoji`.
- **Game Loop**: The primary loop that:
    - Updates the screen.
    - Creates and moves moods.
    - Checks for collisions and handles mood impact.
    - Ends the game based on timer or mood level conditions.

### 3. Helper Functions

- `display_game_over(screen, win=False)`: Displays a "You Won!" or "Game Over!" message based on the game's outcome.

---

## License

This project is licensed under the MIT License. See `LICENSE` file for details.
