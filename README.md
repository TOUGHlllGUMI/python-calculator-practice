# Simple Calculator

A simple Python calculator for practicing GitHub workflows.

## Usage

```python
from calculator import add, subtract, multiply, divide

add(2, 3)       # 5
subtract(5, 3)  # 2
multiply(4, 3)  # 12
divide(10, 2)   # 5.0
```

## Features

- Addition
- Subtraction
- Multiplication
- Division (raises an error on divide by zero)

## Interactive CLI

Run the calculator interactively from the terminal:

```bash
python main.py
```

Enter calculations in the form `<number> <+|-|*|/> <number>` (e.g. `3 + 4`), or type `q` to quit.
