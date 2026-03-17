# 🚢 Battleship

A terminal-based Battleship game in Python where you face off against a CPU opponent.

---

## How to Play

```bash
python main.py
```

On each turn, enter the **row (Latitud)** and **column (Longitud)** to fire a shot at the CPU's board.

---

## Game Setup

- **Board:** 10×10 grid
- **Ships per player:** 3×size-2, 2×size-3, 1×size-4
- Ships are placed **randomly** at game start

---

## Board Legend

| Symbol | Meaning |
|--------|---------|
| `[ ]`  | Empty cell |
| `[O]`  | Your ship |
| `[X]`  | Hit 🔴 |
| `[-]`  | Miss 🔵 |

> The CPU's ships are hidden — no cheating!

---

## Win Condition

Sink all enemy ships before the CPU sinks yours.

---

## File Structure

```
├── main.py     # Game loop & display
└── utils.py    # Board logic, ship placement, shot handling
```

---

## Requirements

```bash
pip install numpy
```
