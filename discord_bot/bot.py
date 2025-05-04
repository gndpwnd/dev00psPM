# discord_bot/bot.py

import os
import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
N8N_API_BASE = os.getenv("N8N_API_BASE")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

def send_to_agent(topic, url, prompt):
    payload = {
        "topic": topic,
        "prompt": prompt,
        "reasoning": f"Auto-generated via /{topic} command"
    }
    try:
        response = requests.post(f"{N8N_API_BASE}/{url}", json=payload)
        return response.json() if response.status_code == 200 else f"Error: {response.text}"
    except Exception as e:
        return f"Request failed: {str(e)}"

@bot.command(name="idea")
async def idea(ctx, *, prompt):
    response = send_to_agent("idea", "webhook/idea-agent", prompt)
    await ctx.send(f"Response from idea agent: {response}")

@bot.command(name="implement")
async def implement(ctx, *, prompt):
    response = send_to_agent("implement", "webhook/implement-agent", prompt)
    await ctx.send(f"Response from implement agent: {response}")

@bot.command(name="improve")
async def improve(ctx, *, prompt):
    response = send_to_agent("improve", "webhook/improve-agent", prompt)
    await ctx.send(f"Response from improve agent: {response}")

if __name__ == "__main__":
    bot.run(TOKEN)