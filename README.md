# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
The game's purpose is to provide a number guessing game where players try to guess a secret number within a limited number of attempts, with hints to guide them higher or lower, and scoring based on performance.

- [x] Detail which bugs you found.
Bugs found: 1) Secret number changed on every submit due to Streamlit reruns. 2) Hints were incorrect because messages were swapped ("Too High" said "Go HIGHER!"). 3) Out-of-bounds guesses were allowed without validation. 4) Logic was mixed with UI in app.py.

- [x] Explain what fixes you applied.
Fixes: 1) Updated new_game to generate secret using difficulty range and reset state properly. 2) Corrected hint messages in check_guess. 3) Added range validation in submit logic. 4) Refactored functions to logic_utils.py and imported them. 5) Updated tests to match corrected logic and added new test for hints.

## 📸 Demo

- [x] The fixed game now allows players to guess within the range, provides correct hints, and properly tracks attempts and score. All tests pass, confirming the fixes work.

## 🚀 Stretch Features

- [x] Challenge 1: Advanced Edge-Case Testing - Added test_hint_message_correctness to verify hints guide correctly. Pytest results: 4 passed in 0.04s (all tests pass).
