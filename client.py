## QUOTE BOT

import discord

class myClient(discord.Client):
    # Coroutine to login
    async def on_ready(self):
        print(f'Hello! Logged in as {client.user}'.format(client))

 # Coroutine to answer messages
    async def on_message(self, ctx):
        if ctx.author == client.user:
            return
        elif ctx.content.startswith('hello'):
            await ctx.channel.send('Good to see ya!')
        elif ctx.content.startswith('Buenas'):
            await ctx.channel.send('¡Hola! ¿Qué tal estás?')       

client = myClient()
client.run('OTcxNzcyNTUzMDQ5ODI1MzAw.GCL6Em.YPrqREdgvKmRQeh6_6g6LCDmCmp7cKcjod4kac')


## END