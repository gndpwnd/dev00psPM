import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def normalize_github_url(url):
    if url.startswith("http://"):
        url = url.replace("http://", "https://", 1)
    if url.startswith("https://"):
        return url
    elif url.startswith("github.com/"):
        return f"https://{url}"
    else:
        if '/' in url:
            return f"https://github.com/{url}"
        else:
            return None

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user.name}")

@bot.command()
async def idea(ctx, *, prompt):
    print(f"Would send to N8N - Topic: idea, Prompt: {prompt}")
    n8n_response = "n8n response goes here"
    await ctx.send(n8n_response)

@bot.command()
async def implement(ctx, *, prompt):
    if 'name:' not in prompt:
        await ctx.send("Please include a project name using 'name:projectname' in your message.")
        return
    try:
        _, rest = prompt.split('name:', 1)
    except ValueError:
        await ctx.send("Invalid format. Use 'name:projectname' followed by your prompt.")
        return
    rest = rest.strip()
    if ' ' in rest:
        name, prompt_text = rest.split(' ', 1)
    else:
        name = rest
        prompt_text = ''
    print(f"Name sent to n8n: {name}")
    print(f"Prompt sent to n8n: {prompt_text}")
    n8n_response = "n8n response goes here"
    await ctx.send(n8n_response)

@bot.command()
async def improve(ctx, *, prompt):
    if 'git:' not in prompt:
        await ctx.send("Please include a GitHub repository using 'git:repo_url' in your message.")
        return
    try:
        _, rest = prompt.split('git:', 1)
    except ValueError:
        await ctx.send("Invalid format. Use 'git:repo_url' followed by your prompt.")
        return
    rest = rest.strip()
    if ' ' in rest:
        git_part, prompt_text = rest.split(' ', 1)
    else:
        git_part = rest
        prompt_text = ''
    normalized_url = normalize_github_url(git_part)
    if not normalized_url:
        await ctx.send("Invalid GitHub URL format. Use 'git:user/repo', 'git:github.com/user/repo', or 'git:https://...'.")
        return
    print(f"Git URL sent: {normalized_url}")
    print(f"Prompt sent: {prompt_text}")
    n8n_response = "n8n response goes here"
    await ctx.send(n8n_response)

@bot.command()
async def usage(ctx):
    embed = discord.Embed(title="Available Commands", color=0x00ff00)
    embed.add_field(name="!idea <prompt>", value="Submit an idea", inline=False)
    embed.add_field(name="!implement name:<projectname> <prompt>", value="Implement a project with a specified name", inline=False)
    embed.add_field(name="!improve git:<repository> <prompt>", value="Suggest improvements for a GitHub repository", inline=False)
    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run(TOKEN)