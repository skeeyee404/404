import discord
import asyncio
import itertools
import os

TOKENS = [
os.getenv("TOKEN1"),
os.getenv("TOKEN2"),
os.getenv("TOKEN3"),
os.getenv("TOKEN4")
]

TOKENS = [t for t in TOKENS if t]

VOICE_CHANNEL_ID = 1506758202283266110

STATUS_MESSAGES = [
"gg/404services",
"Kalitenin Tek Adresi",
"7/24 Kesintisiz Hizmet",
"404 Services Farkıyla!"
]

async def run_bot(token):
intents = discord.Intents.default()
client = discord.Client(intents=intents)

```
async def status_task():
    await client.wait_until_ready()
    msgs = itertools.cycle(STATUS_MESSAGES)

    while not client.is_closed():
        await client.change_presence(
            activity=discord.Game(name=next(msgs))
        )
        await asyncio.sleep(15)

@client.event
async def on_ready():
    print(f"✅ {client.user} giriş yaptı")

    asyncio.create_task(status_task())

    channel = client.get_channel(VOICE_CHANNEL_ID)

    if channel:
        try:
            await channel.connect()
            print(f"🎧 {client.user} ses kanalına bağlandı")
        except Exception as e:
            print(f"❌ Ses bağlantı hatası: {e}")

await client.start(token)
```

async def main():
await asyncio.gather(*(run_bot(t) for t in TOKENS))

asyncio.run(main())
