# Character Input

**Solution to Exercise 1: Character Input**
from [Practice Python](https://www.practicepython.org/exercise/2014/01/29/01-character-input.html)
(January 29, 2014)

## What the exercise asks for

Create a program that:

- Asks the user for name and age
- Prints a message telling them the year they will turn 100

**Extras:**
1. Ask for another number → print the message that many times
2. Print each message on a separate line

> **Important note from the site:**
> The original exercise expects you to **hard-code the year** (so it becomes outdated next year).
> For a more future-proof version using current year dynamically, see Exercise 39.
> → This solution deliberately uses `datetime.date.today()` to make it always correct.

## Features of this implementation

- Full input validation (no crash on letters, negatives, etc.)
- Re-prompts until valid positive integer is entered for age and repeat count
- Handles edge case: age ≥ 100 → special message
- Clean, modular code with separate functions
- Uses real current year (not hard-coded 2014 or whatever)
- No external dependencies – pure Python 3

## How to run

```bash
# Clone the repo (or just download the file)
git clone https://github.com/M-Pourya87/Python-Exercises/practicepython/Character-Input.git
cd Character-Input

# Run it
python main.py
# or
python3 main.py
