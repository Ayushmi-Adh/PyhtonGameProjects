# Python Games Collection

This repository contains three simple game implementations using Python and the Turtle graphics library.
![giphy](https://github.com/Ayushmi-Adh/PyhtonGameProjects/assets/132826306/84704a6c-e2d0-4964-97a6-d66f0206f7b1)

## Table of Contents:

- [Introduction](#introduction)
- [Games](#games)
  - [Snake Game](#snake-game)
  - [Turtle Race Game](#turtle-race-game)
  - [Pong Game](#pong-game)
- [How to Play](#how-to-play)
- [Code Structure](#code-structure)
- [Suggestions for Improvement](#suggestions-for-improvement)
- [License](#license)

## Introduction:

This repository showcases Python games that offer a blend of classic arcade experiences, including Snake, Turtle Race, and Pong.

## Games:

### Snake Game:
![snake-game](https://github.com/Ayushmi-Adh/PyhtonGameProjects/assets/132826306/610fd141-229d-431f-8e5d-14a1c483683e)

#### Introduction:

Snake Game is a classic arcade game where the player controls a snake to eat food and grow longer. The game continues until the snake collides with the boundaries or itself.

#### Features:

- Player-controlled snake movement
- Food generation and consumption
- Score tracking

#### How to Play:

1. Run the Python script.
2. Use the arrow keys to control the snake's movement.
3. Eat the food to increase your score and snake length.
4. The game ends when the snake collides with the boundaries or itself.

#### Code Structure

The code is organized into several files:

- `main_snake.py`: The main script that sets up the game.
- `snake.py`: Contains the `Snake` class for player-controlled snake movement.
- `food.py`: Contains the `Food` class for food generation.
- `score.py`: Contains the `Score` class for tracking scores.

#### Suggestions for Improvement

- Implement additional features like levels, obstacles, or a game over screen.
- Add a delay for the game over screen to improve user experience.
- Refactor code for better modularity and readability.


### Turtle Race Game:
![raw](https://github.com/Ayushmi-Adh/PyhtonGameProjects/assets/132826306/8681102f-2b3e-4e26-81c1-660797502353)

#### Introduction

Turtle Race Game is a fun and interactive race between turtles. Players can choose a turtle color and place bets on which turtle will win the race.

#### Features

- Turtle race simulation
- User input for selecting a betting turtle
- Text input for placing bets

#### How to Play

1. Run the Python script.
2. Input your bet by providing a turtle color.
3. Observe the turtle race.
4. The game will announce the winner, and you'll be notified if your bet was correct.

#### Code Structure

The code is organized into several files:

- `main_turtle_race.py`: The main script that sets up the race.
- `turtle_race.py`: Contains the race logic and turtle creation.
- `input_handling.py`: Contains user input handling for placing bets.

#### Suggestions for Improvement

- Implement a more sophisticated betting system with virtual currency.
- Enhance the game by adding animations or a graphical interface.
- Allow players to place bets on multiple turtles.


### Pong Game:
![R](https://github.com/Ayushmi-Adh/PyhtonGameProjects/assets/132826306/8a53d4aa-9a58-43df-a2b3-a0807c9c7d75)

#### Introduction

Pong Game is a simple implementation of the classic Pong game using Python and the Turtle graphics library.

#### Features

- Player vs. Player gameplay
- Basic ball and paddle collision detection
- Score tracking

#### How to Play

1. Run the Python script.
2. Use the specified keys to control the paddles.
3. Score points by hitting the ball past the opponent's paddle.
4. The game ends when a certain score is reached or when the user decides to exit.

#### Code Structure

The code is organized into several files:

- `main_pong.py`: The main script that sets up the game.
- `paddles.py`: Contains the `Paddle` class for player-controlled paddles.
- `ball.py`: Contains the `Ball` class for the game ball.
- `scoreboard.py`: Contains the `Score` class for tracking scores.

#### Suggestions for Improvement

- Implement additional features like power-ups, different ball speeds, or AI opponents.
- Improve code readability and maintainability with comments and modularization.
- Add an end game condition for better user experience.

