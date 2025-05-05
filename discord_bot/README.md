# Discord Bot

A simple Discord bot for managing development projects via commands. Parses parameters for project names and GitHub URLs.

---

## Discord Bot Setup

To set up your Discord bot to interact with the Dev00ps agent suite:

### 1. Create Your Bot on Discord
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)  
2. Click **"New Application"**  
3. Name it something like `dev00psPM-bot`  
4. Navigate to the **"Bot"** tab on the left sidebar:  
   - Reset Token  
   - Enable **"Server Members Intent"**  
   - Enable **"Message Content Intent"**  

### 2. Set Up Bot Permissions
1. Navigate to the **"OAUTH2"** tab:  
   - Under **"SCOPES"**, select `bot`  
   - Under **"BOT PERMISSIONS"**, select:  
     ```plaintext
     View Channels
     Send Messages
     Read Message History
     ```  
2. Copy the generated URL to invite the bot to your server.

---

## Bot Functionality Overview

### Core Commands

1. **`!idea <prompt>`**  
   Submit a project idea.  
   **Example**:  
   ```bash
   !idea A weather app with cat-themed UI
   ```  
   *Output*: Sends prompt to n8n.

2. **`!implement name:<project_name> <prompt>`**  
   Start a named project.  
   **Example**:  
   ```bash
   !implement name:cat-weather-app Build a weather app with cat animations
   ```  
   *Output*:  
   ```plaintext
   Name sent: cat-weather-app
   Prompt sent: Build a weather app with cat animations
   ```

3. **`!improve git:<repo> <prompt>`**  
   Suggest GitHub repo improvements.  
   **Example**:  
   ```bash
   !improve git:user/cat-weather-app Add dark mode
   ```  
   *Output*:  
   ```plaintext
   GitHub URL: https://github.com/user/cat-weather-app
   Prompt sent: Add dark mode
   ```

4. **`!usage`**  
   Show command help:  
   ```plaintext
   !idea <prompt>                   | Submit an idea
   !implement name:<name> <prompt>  | Start a named project
   !improve git:<repo>  <prompt>    | Suggest project improvements
   ```

---

## Setup

1. **Install dependencies**:  
   ```bash
   pip install discord.py python-dotenv
   ```

2. **Add bot token to `.env`**:  
   ```plaintext
   DISCORD_TOKEN=your_bot_token_here
   ```

3. **Run the bot**:  
   ```bash
   python bot.py
   ```

---

**Project Structure**:  
```plaintext
discord_bot/
├── bot.py              # Main bot logic
└── .env                # Environment variables
```