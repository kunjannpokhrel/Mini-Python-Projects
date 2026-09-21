# Mini Python Projects

A collection of small Python projects built while learning and strengthening my Python programming fundamentals.

The goal of this repository is to practice programming concepts by building projects from scratch and to improve my problem solving.

## Projects

| Project                  | Description                                                                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Alarm**                | A simple alarm program that checks the current time and plays an alert when the set time is reached.                                      |
| **Calculator**           | A command-line calculator supporting basic arithmetic, powers, logarithms, square roots, natural logarithms, and trigonometric functions. |
| **Currency Converter**   | Converts currencies using live exchange-rate data from the Frankfurter API.                                                               |
| **Emoji Converter**      | Converts emojis to their descriptions and searches for emojis using text.                                                                 |
| **Math Quiz**            | A timed math quiz with difficulty levels, randomly generated questions, scoring, and input validation.                                    |
| **Number Guessing Game** | A number guessing game with multiple difficulty levels, hints, guess tracking, and input validation.                                      |
| **Password Generator**   | Generates random passwords using lowercase letters, uppercase letters, numbers, and special characters.                                   |
| **Rock Paper Scissors**  | A Rock Paper Scissors game with a configurable winning score, score tracking, random computer moves, and input validation.                |
| **Timer**                | A command-line countdown timer with minute/second handling and sound effects.                                                             |

## External Tools & Libraries

Some projects use Python libraries and external services:

* **Requests** — for making HTTP requests
* **Frankfurter API** — for currency exchange-rate data
* **Random** — for random numbers and selections
* **Datetime** — for working with the current time
* **Time** — for delays and timing
* **Winsound** — for Windows sound effects
* **String** — for character sets used in password generation
* **Math** — for mathematical operations including powers, logarithms, square roots, and trigonometric functions
* **Demoji** — for finding and identifying emojis

## Requirements

The following external Python packages are required by specific projects:

| Project                | Package    | Installation           |
| ---------------------- | ---------- | ---------------------- |
| **Currency Converter** | `requests` | `pip install requests` |
| **Emoji Converter**    | `requests` | `pip install requests` |
| **Emoji Converter**    | `demoji`   | `pip install demoji`   |

### Install Dependencies

Install the required packages with:

```bash
pip install requests demoji
```

### Built-in Python Modules

The following modules are included with Python and do not require installation:

| Module     | Used In                                                                                                    |
| ---------- | ---------------------------------------------------------------------------------------------------------- |
| `datetime` | Alarm                                                                                                      |
| `time`     | Alarm, Math Quiz, Number Guessing Game, Password Generator, Rock Paper Scissors, Timer                     |
| `winsound` | Alarm, Currency Converter, Math Quiz, Number Guessing Game, Password Generator, Rock Paper Scissors, Timer |
| `math`     | Calculator                                                                                                 |
| `random`   | Math Quiz, Number Guessing Game, Password Generator, Rock Paper Scissors                                   |
| `string`   | Password Generator                                                                                         |

> **Note:** `winsound` is available on Windows.

## Repository Status

**In development**

This repository will continue to grow as I learn new Python concepts and build more projects.

## Author

**Kunjan Pokhrel**

GitHub: [@kunjannpokhrel](https://github.com/kunjannpokhrel)
