# Py-tetris

A little project using pygame.

## Play

### 1 - Create virtual environment.

```sh
python3 -m venv venv
```

### 2 - Install the dependencies in `requirements.txt`.

```sh
python3 -m pip install -r requirements.txt
```

### 3 - Run

```sh
python3 src/main.py
```

### 4 - Keys

- `space`: hard drop
- `a`: lock tetromino
- `h`: left
- `l`: right
- `j`: down (soft drop)
- `z`: rotate left
- `x`: rotate right
- `k`: rotate 180
- `c`: swap tetromino

## Specifications

Following [this guideline](https://harddrop.com/wiki/Tetris_Guideline)

[Lock delay](https://harddrop.com/wiki/Lock_delay): TO-DO

[Random Generator](https://harddrop.com/wiki/Random_Generator): [TGM randomizer](https://harddrop.com/wiki/TGM_randomizer)

[Rotation System](https://harddrop.com/wiki/Rotation_system): [Super/Standard Rotation System](https://harddrop.com/wiki/SRS)

[Scoring System](https://harddrop.com/wiki/Category:Scoring_Systems): TO-DO

[Tetromino Orientation](https://harddrop.com/wiki/Orientation): Default
