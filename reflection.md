# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
The hint were not good
When starting a new game, it didnt let me submit
The difficulty is wrong
The update scoring was inconsistent
  (for example: "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
only copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
it correctly gave me the suggestion for the game not being able to reset

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
It pointed out the incorrect function when I asked about the new game bug
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I run the app then test out the bugs
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One of the test was testing the hint system, check_guess(50, 50), check_guess(60, 50), check_guess(40, 50).
- Did AI help you design or understand any tests? How?
The AI did help me design the tests. It told me to test out each of the possible scenarios for check_guess and parse_guess.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because the app reruns the whole app everytime I interact with it. It fix it, you need to use session state to remember things.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Imagine you are playing a video game and everytime you make an interaction, the whole game crash and reset from start, it is a  Streamlit "reruns". A session state is a save file, that keep your progress even when your game reset.
- What change did you make that finally gave the game a stable secret number?
The change was to wrap the secret number in st.session_state, so the only way for it to generate a random number is when one doesn't exist
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I would commit regularly in my next project
- What is one thing you would do differently next time you work with AI on a coding task?
I would definitly try to do testing properly next project
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This is the first time I use the copilot AI in my coding project. I think this is a better use of AI because I also take in your code file as context.