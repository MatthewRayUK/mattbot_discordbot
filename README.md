# Discord Bot

<img src="logo.png" alt="Bot Logo" width="200" height="200">

This is a simple Discord bot that allows users to participate in a quiz with multiple-choice questions. The bot picks a random quiz question from a predefined list and sends it to users. Users can respond with their answer by typing `!answer [option number]` to get feedback on whether they were correct.

It also allows users to share their progress on the course - 100 Days of Code using a command `!progress [day completed number]`

## Quiz Features

- **Quiz Commands**:
  - `!quiz`: Starts a new quiz with a random question.
  - `!answer [option number]`: Users can respond with the number of the option they think is correct.
  
- **Real-Time Feedback**: After users submit their answer, the bot lets them know whether they were correct or not.

- **Multiple-Choice Options**: Each quiz question has four options, and the bot uses emojis (1️⃣, 2️⃣, 3️⃣, 4️⃣) to represent the choices.

- **User Interaction**: The bot gives users a chance to answer and provides responses based on whether their answer was correct.

## Progress Features
  - `!progress int`: shares a message with the channel stating you have made progress on day x (whatever int is used). 

## Setup

### Prerequisites

- Python 3.x
- [discord.py](https://discordpy.readthedocs.io/en/stable/) library
- A Discord bot token

### Commands

- `!quiz`: Starts a new quiz and sends the quiz question to the channel.
- `!answer [option number]`: Respond with the option number you think is correct (e.g., `!answer 1`).

### Example

```txt
User: !quiz
Bot: 🎉 Welcome to today's quiz! 🎉

Here's how to play:
💻 Type !answer [your option number] to answer the question. E.g. !answer 1
👀 The options will be listed below.
💨 Be quick! Answer correctly to get a shoutout! 🚀

**Quiz of the Day**
What is the data type of 3.14?
1️⃣ --> int
2️⃣ --> float
3️⃣ --> str
4️⃣ --> bool
```


```txt
User: !progress 4
Bot: 🥳 @Matthew just completed Day 71 - Keep the code flowing, you’re doing amazing!
```
