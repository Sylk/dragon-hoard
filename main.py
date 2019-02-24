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
    # credit giving structure: credits (give, request, destroy, rob) @snowflakeUserId creditAmount
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

        # start variable of creditRequest = message.content
        # check to see if there is a second parameter


#   if second param doesnt exist ask 'what would you like do with credits? Options: Give, Request, Destroy, Rob'
#     wait for a response
#     check response to see if it doesn't containt (give, request, destroy, rob)
#       then return 'Transaction ended.'
#     append to new message content to credit request

        # if third param doesn't exist ask 'who would you like' second param ' credits to or from?'
        if credit_operation['tagged_user'] is None or (credit_operation['tagged_user'].startswith("<@") and credit_operation['tagged_user'].endswith(">") and len(credit_operation['tagged_user']) == 21):
            print ('Second parameter is invalid')
#     a recursive loop that checks that i has been called less than three times
#       wait for a user based response
#       if the response wasn't user based then reply 'Invalid transaction recipient'
#       recursively call this with
#     assume we have a good parameter now and get the tagged_user credit balance
        tagged_balance = credit_vault.read()
        credit_operation["tagged_balance"] = tagged_balance

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
client.run(DISCORD_TOKEN)
