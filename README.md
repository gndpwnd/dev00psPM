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
# Wait until n8n is healthy
until [ "$(docker inspect -f '{{.State.Health.Status}}' $(docker compose ps -q n8n))" == "healthy" ]; do
  echo "Waiting for n8n to become healthy..."
  sleep 5
done

# Then run your import once it's ready
docker compose run --rm import-agents
```

## Development

Run n8n locally with Docker:
```bash
docker volume create n8n_data

docker run -it --rm --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  -e N8N_BASIC_AUTH_ACTIVE=true \
  -e N8N_BASIC_AUTH_USER=admin \
  -e N8N_BASIC_AUTH_PASSWORD=admin \
  -e N8N_HOST=localhost \
  -e N8N_PORT=5678 \
  -e N8N_PROTOCOL=http \
  -e N8N_RUNNERS_ENABLED=true \
  docker.n8n.io/n8nio/n8n
```

Remove data
```bash
docker volume rm n8n_data
```
