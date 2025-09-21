- ### Title: Number Guessing Game (with Difficulty Levels & ANSI Stylesheet)

---

### Short Description
- A simple **Number Guessing Game** built within Python.
- The player must guess the randomly chosen number within a set number of attempts (depending on difficulty).
- The game uses **ANSI escape codes** to add colors and styles for a more engaging terminal experience.

---

### Features
- Multiple **Difficulty Levels**
  - **Easy**: Range 1-10, unlimited attempts
  - **Medium**: Range 1-50, 10 attempts
  - **Hard**: Range 1-100, 7 attempts
- **Colored feedback** using ANSI escape codes:
  - Success messages in **green**
  - Hints (**Too high / Too low**) in **Yellow/Magenta**
  - Game Over in **Bold Red**
- A Clean ANSI "stylesheet" class for reusable styles

### How to Run
- Make sure you have **Python 3** installed.
- Clone this repository or copy the code onto a file.
- Run the game:
  ```bash
  python number_guess.py

---

### License
- This project is licensed under the MIT License.