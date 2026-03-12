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

- [ ] Describe the game's purpose.
The game is a guess game with diffucilty and attempt and hint.
- [ ] Detail which bugs you found.
The new game button was not change everything back to normal. The advice when guess was not right.
- [ ] Explain what fixes you applied.
The new game button reset the number with the range of difficulty, attempt, history, and status to playing the advice when guess was change.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
<img width="1227" height="845" alt="Screenshot 2026-03-12 at 12 26 24 AM" src="https://github.com/user-attachments/assets/a30f5716-e738-4322-aa59-e8d6b8080192" />



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
