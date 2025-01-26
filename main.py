from quiz import quizzes
from data import my_token, celebrations
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

client = commands.Bot(command_prefix="!", intents=intents)

# Quiz question storage
current_question = {}

# Function to send the quiz when the user types !quiz
@client.command()
async def quiz(ctx):
    global current_question
    current_question = {}  # Clear previous question
    print("Starting a new quiz...")

    # Choose a random quiz from  list
    quiz = random.choice(quizzes)
    current_question = quiz

    # Tell users how to play before the question
    instructions = "🎉 Welcome to today's quiz! 🎉\n\n" \
                   "Here's how to play:\n" \
                   "💻 Type !answer [your option number] to answer the question. E.g. !answer 1\n" \
                   "👀 The options will be listed below.\n" \
                   "💨 Be quick! Answer correctly to get a shoutout! 🚀\n\n"

    # Send the question and answer choices
    question_text = f"**Quiz of the Day**\n{quiz['question']}\n"
    for idx, option in enumerate(quiz['options'], 1):
        question_text += f"{get_emoji_for_option(idx)} --> {option}\n"

    # Send the instructions and the question
    await ctx.send(instructions + question_text)

# Function to map option numbers to emojis
def get_emoji_for_option(option_number):
    emoji_map = {
        1: "1️⃣",
        2: "2️⃣",
        3: "3️⃣",
        4: "4️⃣"
    }
    return emoji_map.get(option_number, "❓")

# Define the !answer command
@client.command()
async def answer(ctx, option_number: int):
    global current_question
    if current_question:  # Check if there is a current question
        print(f"Answer received: {option_number}")
        correct_answer_index = current_question['answer_index']
        if option_number - 1 == correct_answer_index:  # -1 so user answer matches index
            await ctx.send(f"🎉 {ctx.author.mention} got today's quiz question correct - way to go! 🎉")
        else:
            await ctx.send(f"😞 {ctx.author.mention} got today's quiz question incorrect. Better luck next time! 😞")

        # Delete the user's message after they have answered
        await ctx.message.delete()
    else:
        await ctx.send("❓ No quiz is currently running. Please type !quiz to start a new quiz!")

# Defines the !progress function
@client.command()
async def progress(ctx, day: int):
    await ctx.send(f"\n🥳 {ctx.author.mention} just completed Day {day} - {random.choice(celebrations)}\n")
    await ctx.message.delete()

# Start the task when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run(my_token)
