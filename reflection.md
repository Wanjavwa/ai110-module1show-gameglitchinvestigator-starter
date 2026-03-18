# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

--- When I first ran the game for every figure I put it kept saying go lower and lower even though the secret number was higher than all the guesses I put in. Furthermore it allowed me to put in numbers that were out of bounds of the range highlighted in the question and it did not raise any concern or error for this.The second time I ran the code, it completey stopped recording my guesses. Lastly the magic number kept changing every time.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used GitHub Copilot as my main AI teammate, including its Agent mode for refactoring tasks.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Copilot suggested refactoring the core game logic functions (like check_guess and parse_guess) from app.py into logic_utils.py to separate UI from logic. I verified this by running pytest, which passed all tests, and by importing the functions successfully without errors.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The original AI-generated code had incorrect hint messages in check_guess (e.g., "Too High" said "Go HIGHER!" instead of "Go LOWER!"). I verified this by running the game and seeing that hints misled players, and by examining the code logic which had swapped messages.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed when pytest ran successfully with all tests passing, and when running the Streamlit app showed the expected behavior without errors.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran pytest on the test_game_logic.py file, which showed that the check_guess function now correctly returns "Too High" with "Go LOWER!" for guesses above the secret, confirming the hint logic was fixed.

- Did AI help you design or understand any tests? How?
Yes, Copilot helped generate a new test case (test_hint_message_correctness) that specifically checks the hint messages contain the correct guidance words, ensuring the fix was robust.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns are like refreshing the entire app every time you interact with it, such as clicking a button, which can reset variables if not stored properly. Session state is like a persistent storage that survives reruns, so you can keep track of things like scores or game progress across interactions.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to reuse the habit of running tests after every fix to ensure changes work correctly.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would verify AI suggestions more thoroughly before implementing, especially for logic that might have edge cases.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated code can have subtle bugs that need careful review, and collaborating with AI as a teammate can speed up fixes but requires critical thinking to avoid blindly accepting suggestions.
