# N8PM Dev00ps

A suite of N8N-based agents that manage full-stack DevOps and project management tasks, controlled through a Discord bot interface.

---

## Discord Bot Setup

To set up your Discord bot to interact with the Dev00ps agent suite:

### 1. Create Your Bot on Discord

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"**
3. Name it something like `Dev00ps Agent Bot`
4. Go to **"Bot"** in the sidebar and click **"Add Bot"**
5. Under "Token", click **"Copy"** — store this securely (you'll use it in your `.env` or `config.py`)

### 2. Set Up Bot Permissions

1. Under the **"OAuth2" > "URL Generator"** tab:
   - Scopes: `bot`, `applications.commands`
   - Bot Permissions:
     - `Send Messages`
     - `Read Message History`
     - `Use Application Commands` (for slash commands)

2. Copy the generated URL and use it to **invite the bot to your server**

---

## Bot Functionality Overview

The bot acts as an interface to trigger or interact with agents in your N8N system. It supports the following primary slash commands:

### `/idea`

Send a new project idea to the appropriate agent (e.g., for project scoping or backlog creation).

- **Mapped Agent:** `idea-agent` (N8N workflow)
- **Usage:**

    ```bash
    /idea description: "Build an AI-powered DevOps assistant"
    ```

### `/implement`

Trigger a project implementation task, such as spinning up a new stack or VM.

- **Mapped Agent:** `implement-agent`
- **Usage:**

    ```bash
    /implement task: "Create environment for payment API"
    ```

### `/improve`

Send improvement suggestions to agents that monitor or refine existing systems.

- **Mapped Agent:** `improve-agent`
- **Usage:**

    ```bash
    /improve service: "Staging", suggestion: "Add error alerting"
    ```

Each of these commands triggers the appropriate N8N agent via an API call or webhook and returns a confirmation or response directly in Discord.

---

## Project Structure (Relevant to Discord Bot)

```
discord_bot/
├── bot.py              # Sets up bot and commands
├── config.py           # Stores bot token, agent mappings
├── commands/
│   ├── idea.py         # /idea command handler
│   ├── implement.py    # /implement command handler
│   └── improve.py      # /improve command handler
└── utils/
    └── n8n_api.py      # Handles interaction with N8N API
```


