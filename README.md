# dev00psPM

> N8N enabled full stack devops
> Chat interface through discord

## Environment Setup

sample .env file

```bash
DISCORD_TOKEN=your_discord_token
N8N_API_BASE=http://n8n:5678
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=adminpass
```

## Deploy N8N and Discord Bot

```bash
docker-compose up -d
```