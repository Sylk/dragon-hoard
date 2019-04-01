import discord
from discord.ext import commands
import sqlite3
import random
import datetime
import asyncio


class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect('currency.db', detect_types=sqlite3.PARSE_DECLTYPES)
        self.c = self.conn.cursor()

    def check_balance(self, user_id):
        self.c.execute("SELECT balance FROM currency WHERE UID = ?", [user_id])
        return self.c.fetchone()

    def modify_balance(self, author, target, amount):
        self.c.execute("UPDATE CURRENCY SET balance = balance + ? where UID = ?", [amount, author])
        self.c.execute(
            "UPDATE CURRENCY SET balance = balance + ? where UID = ?", [-amount, target])
        self.conn.commit()

    @commands.group()  # %credits
    async def credits(self, ctx):
        if ctx.invoked_subcommand is None:
            author_balance = self.check_balance(ctx.author.id)
            await ctx.send(f'You currently have {author_balance[0]} credits')

    @credits.command()
    async def give(self, ctx, targeted_user: discord.Member, amount: int):  # %credits give
        if ctx.author == targeted_user:
            await ctx.send("You can't give to yourself")
            return 0

        author_balance = self.check_balance(ctx.author.id)
        if author_balance[0] < amount:
            await ctx.send("You don't have enough gold")
            return 0

        if amount > 0:
            self.modify_balance(ctx.author.id, targeted_user.id, -amount)
        else:
            await ctx.send("Enter in a value greater than 1")

    @credits.command()
    async def request(self, ctx, targeted_user: discord.Member, amount: int):
        if ctx.author == targeted_user:
            await ctx.send("You can't request from yourself")
            return 0

        target_balance = self.check_balance(targeted_user.id)
        if target_balance[0] < amount:
            await ctx.send(f"User doesn't have enough, they only have {target_balance[0]}")
            return 0

        if amount > 0:

            def check_reaction(msg):  # defined inside request method so it can use the local target_user variable
                if (msg.content.startswith('$accept') or msg.content.startswith(
                        '$deny')) and msg.author == targeted_user:
                    return True

            await ctx.send(
                f"{ctx.author.mention} requested {amount} from {targeted_user.mention}, type $accept or $deny")

            try:
                response_message = await self.bot.wait_for('message', timeout=20,
                                                           check=check_reaction)  # takes a predicate

            except asyncio.TimeoutError:
                await ctx.send("Request timed out!")

            else:
                if response_message.content.startswith(
                        '$deny'):  # Use a different prefix, otherwise the bot will get a command error
                    await ctx.send(f"{targeted_user.mention} denied {ctx.author.mention}'s request for {amount}")

                elif response_message.content.startswith(
                        '$accept'):  # This could be changed to become a command that checks a queue of some kind but this seems better for now
                    await ctx.send(f"{targeted_user.mention} approved {ctx.author.mention}'s request for {amount}")
                    self.modify_balance(ctx.author.id, targeted_user.id, amount)

    @credits.command()
    async def destroy(self, ctx, amount: int):
        author_balance = self.check_balance(ctx.author.id)
        if author_balance[0] < amount:
            await ctx.send("You don't have enough gold to ")
            return 0

        if amount > 0:
            self.c.execute("UPDATE CURRENCY SET balance = balance + ? where UID = ?", [-amount, ctx.author.id])
            await ctx.send(f"Destroyed {amount} of {ctx.author.mention}'s gold")
            self.conn.commit()
        else:
            await ctx.send("Don't try to destroy a negative amount")

    @credits.command()
    async def rob(self, ctx, targeted_user: discord.Member, amount: int):

        self.c.execute("SELECT rob FROM currency WHERE UID = ?", [targeted_user.id])
        rob_date = self.c.fetchone()[0]

        if ctx.author == targeted_user:
            await ctx.send("You can't rob yourself")
            return 0

        target_balance = self.check_balance(targeted_user.id)
        if target_balance[0] < amount:
            await ctx.send(f"User doesn't have enough, they only have {target_balance[0]}")
            return 0

        if (datetime.datetime.now() - rob_date) >= datetime.timedelta(days=1):  # checks if its been one or more days
            roll_chance = 50
            user_roll = random.randint(0, 100)

            await ctx.send(
                f"Rolling against {targeted_user.mention}, type $Run within 20 seconds to improve your chances")

            def check_reaction(msg):  # defined inside request method so it can use the local target_user variable
                if msg.content.lower().startswith('$run') and msg.author == targeted_user:
                    return True

            try:
                await self.bot.wait_for('message', timeout=30, check=check_reaction)  # takes a predicate
            except asyncio.TimeoutError:  # On timeout receives a timeout error, if we don't hit the time out, then the user ran
                pass
            else:
                roll_chance = random.randint(50, 75)
                await ctx.send(f"{targeted_user.name} ran!")

            await ctx.send(f"Roll chance against {targeted_user.name} is %{roll_chance}!")

            if user_roll > roll_chance:  # win
                await ctx.send(f"Successfully rolled {user_roll} against {roll_chance}!")

                self.modify_balance(ctx.author.id, targeted_user.id, amount)  # transfer balance

                self.c.execute("UPDATE CURRENCY SET rob = ? where UID = ?",
                               [datetime.datetime.now(), targeted_user.id])  # set new rob date
                self.conn.commit()

                await ctx.send(f"{ctx.author.name} took {amount} from {targeted_user.name}!")

            elif user_roll == roll_chance:  # tie
                await ctx.send(f"Tied roll! {user_roll} against {roll_chance}!")

            else:  # loss
                loss_amount = amount // 2
                author_balance = self.check_balance(ctx.author.id)
                if author_balance[0] <= loss_amount:
                    loss_amount = author_balance[0]

                await ctx.send(f"Failed roll! {user_roll} against {roll_chance}!")
                if loss_amount != 0:
                    self.modify_balance(ctx.author.id, targeted_user.id,
                                        -loss_amount)  # lose some amount trying to rob them

                    await ctx.send(f"{ctx.author.name} lost {loss_amount} while running from {targeted_user.name}!")
                else:
                    await ctx.send(f"{ctx.author.name} ran away like the bum they are...")
        else:
            await ctx.send(f"{targeted_user.name} was robbed too recently, stop bullying them!")


def setup(bot):
    bot.add_cog(Currency(bot))
