import discord
import asyncio
import os
import sqlite3


client = discord.Client()
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # TODO: Confirm it's the same user if they go through the giving cycle in each step
    # TODO: Make this more oop friendly or functional and less procedural for legibility sake

    # Show help message when the !credits command is entered
    if message.content.lower() == '!credits':
        await client.send_message(message.channel, 'You\'re currently missing parameters in your request.\n\n' +
                                                   'In order to properly respond we need the following information from your query.\n\n' +
                                                   '(1)!credits (2)Requested Operation (3)Targeted User (4)Credit Amount\n' +
                                                   'Requested operations are [Give, Request, Destroy, Rob]')

    if message.content.lower().startswith('!credits'):
        # explode the given statement
        user_input = message.content.lower().split(" ")

        # TODO: Change this to a correct loop instead of a series of ifs
        # Default values here if they don't exist
        user_input_length = len(user_input)
        default_inputs = [None, None, 0]
        if user_input_length <= 1:
            user_input.append(None)
        if user_input_length <= 2:
            user_input.append(None)
        if user_input_length <= 3:
            user_input.append(0)

        # create command based dictionary to work off of
        credit_operation = {
            "author": message.author,
            "author_balance": 0,
            "operator": user_input[1],
            "tagged_user": user_input[2],
            "tagged_balance": 0,
            "credit_amount": user_input[3]
        }

        # NOTE: Should actually be using sqlite https://docs.python.org/3.7/library/sqlite3.html
        # https://docs.python.org/3.7/library/sqlite3.html#sqlite3.Cursor
        # open the credit vault obtain their credit balance
        credit_vault = sqlite3.connect('creditVault.db')
        cursor = credit_vault.cursor()
        # TODO: Actually locate the authors balance
        author_balance = cursor.executescript("SELECT * WHERE user_id = credit_operation['author']")
        # TODO: If no balance exists then default the balance to 0 and create a new record in the CSV


        # obtain users credit balance
        credit_operation["author_balance"] = author_balance

        # TODO: There is potential to optimize it with a python equivalent of this http://es6-features.org/#RestParameter
        # if second param doesnt exist ask 'what would you like do with credits? Options: Give, Request, Destroy, Rob'
        if (
                credit_operation['operator'] is None or (
                credit_operation['operator'] != 'give'
                or credit_operation['operator'] != 'request'
                or credit_operation['operator'] != 'destroy'
                or credit_operation['operator'] != 'rob')
        ):
            await client.send_message(message.channel, 'Invalid operation parameter, transaction ended.')
            return

        # if third param doesn't exist ask 'who would you like' second param ' credits to or from?'
        if (
                credit_operation['tagged_user'] is None or (
                credit_operation['tagged_user'].startswith("<@")
                and credit_operation['tagged_user'].endswith(">")
                and len(credit_operation['tagged_user']) == 21)
        ):
            await client.send_message(message.channel, 'Invalid transaction recipient, transaction ended.')
            return

        # TODO: Actually locate the authors balance
        tagged_balance = credit_vault.read()
        # TODO: If no balance exists then default the balance to 0 and create a new record in the CSV
        credit_operation["tagged_balance"] = tagged_balance

#     if fourth param doesn't exist
        if isinstance(credit_operation['credit_amount'], int):
            # return 'Transaction ended, invalid credit amount.'
            await client.send_message(message.channel, 'Transaction ended, invalid credit amount.')
            return

#   check the second param against a switch statement
#     case give
#       if creditBalance - creditAmount >= 0
#         if credit_operation['author_balance'] - credit_operation['credit_amount'] >= 0:

#         process csv request against the third param
#         return 'Transaction completed. Remaining balance: ' creditBalance - creditAmount
#             await client.send_message(message.channel, 'Transaction completed. Remaining balance ' + (credit_operation['author_balance'] - credit_operation['credit_amount']))
#       else
#         return 'Insufficient credit balance to process transaction.'
#     case request
#       if snowflakeUserId.creditBalance - creditAmount >= 0
#         apply response message to chat 'Attention to ' @snowflakeUserId '
#         would you like to proccess this transaction? Y/N'
#         wait for a response from given @snowflakeUserId
#         if message.content is not Y
#           return 'Transaction has been declined by ' @snowflakeUserId
#         process csv request against the user who made the request
#         return 'Transaction completed. Remaining balance: ' creditBalance - creditAmount
#       else
#         return 'Insufficient credit balance to process transaction.'
#     case destroy
#     if creditBalance - creditAmount >= 0
#         process csv request against the user who made the request
#         return 'Transaction completed. Remaining balance: ' creditBalance - creditAmount
#       else
#         return 'Insufficient credit balance to process transaction.'
#     case rob
#       check to see if user is capable of robbing user.lastRobbery
#       check to see if snowflakeUserId is capable of being robbed snowflakeUserId.lastRobbed
#       attemptedNumber roll some odds 1 in creditamount to rob said user
#       if randInt numbers between (1, creditAmount) == attemptedNumber
#         return 'Well, there\'s been a robbery, ' @snowflakeUserId ' has been robbed for ' attemptedNumber '.'
#       else
#         return 'Better luck next time, it was a 1 out of ' attemptedNumber ' it\'s all RNG'
#       some zany logic that will use the csv to apply a time date for last attempted robbery and lastRobbed
client.run(DISCORD_TOKEN)
