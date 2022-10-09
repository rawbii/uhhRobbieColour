import asyncio
import random
from discord.ext import commands, tasks
import discord
from discord.utils import get

TOKEN = "BOT_TOKEN"

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!",intents=intents)
typingID = ID_OF_ROLE_WHEN_TYPING
standardID = ID_OF_ROLE_WHEN_INACTIVE
guildID = ID_OF_GUILD/SERVER


#on ready
@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name = "Holders"))



@client.event
async def on_typing(channel,user,when):
    if user.id == USER_ID:
        guild = await client.fetch_guild(guildID)
        role = get(guild.roles, id=int(typingID))
        role2 =  get(guild.roles, id=int(standardID))
        await user.add_roles(role)
        await asyncio.sleep(random.randrange(3,9,1))
        await user.remove_roles(role)
        await user.add_roles(role2)



client.run(TOKEN)
print(client.user.name)