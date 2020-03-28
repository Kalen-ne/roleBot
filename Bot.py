import discord

TOKEN = 'NjYzMjE5MjIxNzQ0MDU4MzY5.Xn8X0A.zSuHZ2T8-NDclqGg3L_XKBxlUwg'

client = discord.Client()

client.event
async def on_message(message):
    if message.content.statswith('!kingariempire'):
        role = discord.utils.get(message.guild.roles, name= '国民')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} ようこそ！'
        await message.channel.send(reply)

client.run(NjYzMjE5MjIxNzQ0MDU4MzY5.Xn8X0A.zSuHZ2T8-NDclqGg3L_XKBxlUwg)
