import discord
import asyncio
import os

client = discord.Client()
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    # if message.content.startswith('!credits'):
    #
    #        await client.send_message(message.channel, '?')
    #        await client.send_message(message.channel, 'Who is cool? Type $name namehere')
    #
    #        # await client.send_message(message.channel, file_object.read())
    #    elif message.content.startswith('!sleep'):
    #        await asyncio.sleep(5)
    #        await client.send_message(message.channel, 'Done sleeping')


@client.event
async def on_message(message):
    # TODO: Give users a structure to use if they say !credits and provide no params
    # INFO: credit giving structure: credits (give, request, destroy, rob) @snowflakeUserId creditAmount
    # if someone says credits
    if message.content.startswith('!credits'):
        # explode the given statement
        user_input = message.content.split(" ")

        # create command based dictionary to work off of
        credit_operation = {
            "author": message.author,
            "author_balance": 0,
            "operator": user_input[1],
            "tagged_user": user_input[2],
            "tagged_balance": 0,
            "credit_amount": user_input[3]
        }

        # open the credit vault obtain their credit balance
        credit_vault = open("creditVault.csv", "w+")
        author_balance = credit_vault.read()

        # obtain users credit balance
        credit_operation["author_balance"] = author_balance

        # TODO: There is potential to optimize it with a python equivalent of this http://es6-features.org/#RestParameter
        # if second param doesnt exist ask 'what would you like do with credits? Options: Give, Request, Destroy, Rob'
        if credit_operation['operator'] is None or (
                credit_operation['operator'] == 'give'
                or credit_operation['operator'] == 'request'
                or credit_operation['operator'] == 'destroy'
                or credit_operation['operator'] == 'rob'):
                # wait for a response
                # check response to see if it doesn't containt (give, request, destroy, rob)
                    # then return 'Transaction ended.'
                    await client.send_message(message.channel, 'Transaction ended')
            # append to new message content to credit request
            credit_operation['operator'] = 'input'

        # TODO: could write the second check as regex
        # if third param doesn't exist ask 'who would you like' second param ' credits to or from?'
        if credit_operation['tagged_user'] is None or (
                credit_operation['tagged_user'].startswith("<@")
                and credit_operation['tagged_user'].endswith(">")
                and len(credit_operation['tagged_user']) == 21):
                    # ask for a valid user
                    # wait for a user based response
                        # if the response wasn't user based then reply 'Invalid transaction recipient'
                    # assume we have a good parameter now and get the tagged_user credit balance
        tagged_balance = credit_vault.read()
        credit_operation["tagged_balance"] = tagged_balance


#     if third param doesn't exist
        if credit_operation['credit_amount'] is None or isinstance(credit_operation['credit_amount'], int):

#       return 'Transaction ended, invalid recipient.'
#   check the second param against a switch statement
#     case give
#       if creditBalance - creditAmount >= 0
        if credit_operation['author_balance'] - credit_operation['credit_amount'] >= 0:

#         process csv request against the third param
#         return 'Transaction completed. Remaining balance: ' creditBalance - creditAmount
            await client.send_message(message.channel, 'Transaction completed. Remaining balance ' + (credit_operation['author_balance'] - credit_operation['credit_amount']))
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
