import discord

TOKEN = ' DISCORD_BOT_TOKEN '

client = discord.Client()

client.event
async def on_message(message):
    if message.content.statswith('!kingariempire'):
        role = discord.utils.get(message.guild.roles, name= '国民')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} ようこそ！'
        await message.channel.send(reply)

client.run(DISCORD_BOT_TOKEN)
