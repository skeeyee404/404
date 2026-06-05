import discord
import asyncio
import itertools

# 1. Bot tokenlerinizi buraya ekleyin
TOKENS = [
    "MTUwNzQ3MTcwMjQzMzcyNjU2NQ.GW4Gyk.Caghjr98OlAayBL0_gSB7AHooFnELHOzG3wpzI",
    "MTUwNzg2ODgzMzg5NTk0MDE5Ng.G-4BBm._AhbOQR6lV4e0iSOz1c4SoKP_d-Ehc7MIAUVL4",
    "MTUwNzY3NzI3MjI4OTU3OTE1OA.Gwo8Y7.q8sHuriZglWYXdc4cBgQgEQTbnelD5JyaB8_Q8",
    "MTUwODU2NDI2NjA3MDgzOTUyMQ.Gx3KTn.ICVaw6Wn9ZAqGttSdSh_CFCA_V9G6siVGN4a_s"
]

# 2. Botların gireceği ses kanalının ID'si
VOICE_CHANNEL_ID = 1506758202283266110

# 3. Sırayla değişecek durum mesajları (İstediğiniz kadar ekleyebilirsiniz)
STATUS_MESSAGES = [
    "gg/404services",
    "Kalitenin Tek Adresi",
    "7/24 Kesintisiz Hizmet",
    "404 Services Farkıyla!"
]

async def run_bot(token):
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    # Arka planda çalışacak olan animasyonlu durum fonksiyonu
    async def status_task():
        await client.wait_until_ready()
        # Mesajları sonsuz bir döngüde (cycle) sırayla alır
        msgs = itertools.cycle(STATUS_MESSAGES)
        
        while not client.is_closed():
            current_status = next(msgs)
            # Durumu "Oynuyor" olarak günceller
            await client.change_presence(activity=discord.Game(name=current_status))
            # Discord sınırlarına takılmamak için 15 saniye bekler (bu süreyi değiştirebilirsiniz)
            await asyncio.sleep(15)

    @client.event
    async def on_ready():
        print(f'✅ {client.user} olarak giriş yapıldı!')
        
        # Durum değiştirme döngüsünü arka planda başlatıyoruz
        client.loop.create_task(status_task())
        
        channel = client.get_channel(VOICE_CHANNEL_ID)

        if channel and isinstance(channel, (discord.VoiceChannel, discord.StageChannel)):
            try:
                await channel.connect()
                print(f"🎧 {client.user.name} ses kanalına başarıyla katıldı!")
            except discord.ClientException:
                print(f"⚠️ {client.user.name} zaten bir ses kanalına bağlı.")
            except Exception as e:
                print(f"❌ {client.user.name} ses kanalına bağlanırken hata: {e}")
        else:
            print(f"❌ {client.user.name} kanalı bulamadı. Botun kanalı görme yetkisi olduğundan emin olun.")

    try:
        await client.start(token)
    except discord.errors.LoginFailure:
        print(f"❌ Geçersiz token, lütfen kontrol edin.")
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")

async def main():
    tasks = [run_bot(token) for token in TOKENS]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    print("🚀 Botlar başlatılıyor, lütfen bekleyin...")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 İşlem kullanıcı tarafından durduruldu.")
