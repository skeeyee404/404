import os
import discord
import asyncio
import itertools

TOKENS = [
os.getenv("TOKEN1"),
os.getenv("TOKEN2"),
os.getenv("TOKEN3"),
os.getenv("TOKEN4")
]

TOKENS = [token for token in TOKENS if token]

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
    messages = itertools.cycle(STATUS_MESSAGES)

    while not client.is_closed():
        try:
            await client.change_presence(
                activity=discord.Game(name=next(messages))
            )
        except Exception as e:
            print(f"Durum güncelleme hatası: {e}")

        await asyncio.sleep(15)

@client.event
async def on_ready():
    print(f"✅ {client.user} giriş yaptı")

    asyncio.create_task(status_task())

    channel = client.get_channel(VOICE_CHANNEL_ID)

    if channel is None:
        print(f"❌ Kanal bulunamadı: {VOICE_CHANNEL_ID}")
        return

    try:
        await channel.connect()
        print(f"🎧 {client.user} ses kanalına bağlandı")
    except discord.ClientException:
        print(f"⚠️ {client.user} zaten bağlı")
    except Exception as e:
        print(f"❌ Ses bağlantı hatası: {e}")

try:
    await client.start(token)
except discord.errors.LoginFailure:
    print("❌ Geçersiz token")
except Exception as e:
    print(f"❌ Hata: {e}")
```

async def main():
tasks = [run_bot(token) for token in TOKENS]
await asyncio.gather(*tasks)

if **name** == "**main**":
asyncio.run(main())
