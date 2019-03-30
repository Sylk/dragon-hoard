import discord
from discord.ext import commands
import platform
import asyncio
import sqlite3
import private_key
import datetime

cog_list = ["cogs.currency"]

print(f'Initializing currency.db')
conn = sqlite3.connect("currency.db", detect_types=sqlite3.PARSE_DECLTYPES)
c = conn.cursor()
c.execute(
    "CREATE TABLE IF NOT EXISTS currency (UID integer PRIMARY KEY, name TEXT, balance INTEGER DEFAULT 0, rob TIMESTAMP)")


class DragonHoard(commands.Bot):
    def __init__(self):
        super().__init__(description="DragonHoard", command_prefix="!", case_insensitive=True, pm_help=False)
        for cog in cog_list:
            self.load_extension(cog)

    def add_user_to_database(self, user):
        c.execute("INSERT OR IGNORE into currency (UID, name, balance, rob) VALUES (?,?,?,?)",
                  [user.id, user.name, 100, datetime.datetime.now()])
        conn.commit()

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

        user_list = self.get_all_members()
        for x in user_list:
            self.add_user_to_database(x)
        # adds current users to database

    async def on_message(self, message):
        if message.author != self.user:  # just stops the bot from noticing its own messages
            pass  # await message.channel.send("fuck you conic")
        await self.process_commands(message)

    async def on_member_join(self, member):  # adds new member to database and welcomes them
        self.add_user_to_database(member)
        await member.guild.channels[1].send(f"Welcome {member.mention}")


if __name__ == "__main__":
    client = DragonHoard()
    client.run(private_key.private_key)
