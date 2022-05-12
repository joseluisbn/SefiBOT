from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler

PREFIX = "!"
OWNER_IDS = [321296622384316416]

class Bot(BotBase):
    def __init__(self):

        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)
    
    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.txt", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
        print("Bot running")
        super().run(self.TOKEN, reconnect=True)
    
    async def on_connect(self):
        print("Bot connected")
    
    async def on_disconnect(self):
        print("Bot disconnected")
    
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            # self.guild = self.get_guild(969238145239502848)
            print("Bot ready")

        else:
            print("Bot reconnected")

    async def on_message(self, message):
        pass

bot =  Bot()