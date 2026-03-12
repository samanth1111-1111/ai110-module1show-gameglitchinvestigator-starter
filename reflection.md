# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---
the hint were backward
the hint need to be lower if number is higher than the number and the hint need to be higher if number is lower than the number
new game only secret number change not the full thing
when new game every thing need to reset
the dificulty not work
the difficulty stay 1 to 100
attempt 1 when refresh
it should be 0
accept negative number
it should accept positive

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
CLaude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I want to make sure the new game put everything back to the way it was and claude suggest add change that put it back I use the code it suggest i made sure it was good by check the game
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
None

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I went to the game and check
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I click new game and i saw if it made everything back to normal it show the code work
- Did AI help you design or understand any tests? How?
The test the ai gave help me learn what I should be doing
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Need to press new game
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Steamlit rerun your entire script whenever. the user interact with the app session state is a tool that let your app remember value between those rerun
- What change did you make that finally gave the game a stable secret number?
change new game to reset it
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Looking at the ai response and read it
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I would tell it what wrong what need to do
- In one or two sentences, describe how this project changed the way you think about AI generated code.
With ai you should alway consider it as a companion not making decision>. Need to read the code each time and understand it.
