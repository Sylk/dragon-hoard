import discord
import asyncio
import os

client = discord.Client()


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
    # credit giving structure: credits (give, request, destroy, rob) @snowflakeUserId creditAmount
    # if someone says credits
    if message.content.startswith('!credits'):
        # explode the given statement
        userInput = message.content.split(" ")
        # obtain their credit balance creditBalance = user.credits
        credit_balance = open("creditVault.csv", "r+")
        # start variable of creditRequest = message.content
        # check to see if there is a second parameter


#   if second param doesnt exist ask 'what would you like do with credits? Options: Give, Request, Destroy, Rob'
#     wait for a response
#     check response to see if it doesn't containt (give, request, destroy, rob)
#       then return 'Transaction ended.'
#     append to new message content to credit request
#   if third param doesn't exist ask 'who would you like' second param ' credits to or from?'
#     a recursive loop that checks that i has been called less than three times
#       wait for a user based response
#       if the response wasn't user based then reply 'Invalid transaction recipient'
#       recursively call this with
#     if third param doesn't exist and i is equal to or greater than 3
#       return 'Transaction ended, invalid recipient.'
#   check the second param against a switch statement
#     case give
#       if creditBalance - creditAmount >= 0
#         process csv request against the third param
#         return 'Transaction completed. Remaining balance: ' creditBalance - creditAmount
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

client.run(os.getenv("DISCORD_TOKEN"))
