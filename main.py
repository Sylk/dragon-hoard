import discord
from discord.ext import commands
import platform
import asyncio
import sqlite3
import private_key


cog_list = ["cogs.currency"]

class DragonHoard(commands.Bot):
    def __init__(self):
        super().__init__(description="DragonHoard", command_prefix="!", case_insensitive=True, pm_help=False)
        for cog in cog_list:
            self.load_extension(cog)

    async def on_ready(self):  # Tells us info about the bot and readys the bot for taking commands
        print(f'Logged in as {self.user.name} (ID:{self.user.id}')
        # Username and ID
        print('--------')
        print(
            f'Current Discord.py Version: {discord.__version__} | Current Python Version: {platform.python_version()}')
        # Discord and Python version
        print('--------')
        print(f'Use this link to invite {self.user.name}:')
        print(f'https://discordapp.com/oauth2/authorize?client_id={self.user.id}&scope=bot&permissions=8')
        # prints a link that you may use to invite to your server


if __name__ == "__main__":
    client = DragonHoard()
    client.run(private_key.private_key)
