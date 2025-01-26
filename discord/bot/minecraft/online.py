import discord
import mcstatus
import asyncio

bot = discord.Client(intents=discord.Intents.default())
server = mcstatus.JavaServer("SERVER_IP")
start_time = asyncio.get_event_loop().time()

async def update_status():
    symbols = ['\\', '|', '/', '|']  
    while True:
        for symbol in symbols:
            try:
                status = server.status()
                max_players = status.players.max
                online_players = status.players.online
                ping = round(status.latency, -1)
                server_status = "Работает"

                elapsed_time = asyncio.get_event_loop().time() - start_time
                hours = int(elapsed_time // 3600)
                minutes = int((elapsed_time // 60) % 60)

                status_message = (
                    f"на онлайн: {online_players} | {max_players} {symbol} "
                    f"Пинг ~ {ping}ms {symbol} "
                    f"{server_status} {symbol} "
                    f"{status.version.name} {symbol} " 
                    f"В сети ~ {hours}ч {minutes}м"
                )

                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status_message))
                await asyncio.sleep(5)
            except Exception:
                status_message = "на статус: Сервер остановлен"
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status_message))

        await asyncio.sleep(5) 

@bot.event
async def on_ready():
    asyncio.create_task(update_status())

bot.run('YOUR_TOKEN')
