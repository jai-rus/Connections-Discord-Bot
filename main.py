import discord
from discord.ext import commands
import logic
import asyncio
import config

intents = discord.Intents.default()
intents.message_content = True

#checks whether user is in game

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print('---------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!play'):
        global word_bank
        word_bank = ("basic", "java", "python", "ruby", "croc", "loafer", "moccasin", "slipper", "boa", "headdress", "pillow", "shuttlecock", "cobra", "inspiration", "lightning", "union")

        gameBoard = logic.Logic.setPositions(word_bank)

        await message.channel.send(gameBoard[0])
        await message.channel.send(gameBoard[1])
        await message.channel.send(gameBoard[2])
        await message.channel.send(gameBoard[3])

        logic.Logic.newGame()

    if message.content.startswith('!answer'):
        completedWords = [0, 0, 0, 0] #Used to see if they already used an answer set
        tries = 4 #Amount of tries the user gets

        while (logic.Logic.inGame()): 
            try:
                guess = await bot.wait_for('message', timeout=500.0)
            except asyncio.TimeoutError:
                return await message.channel.send("You took too long")

            check = logic.Logic.checkAnswer(guess.content, word_bank)

            #checks if its a correct answer
            if (check[0]): 
                if (completedWords[check[1]] == 0): #checks if it already exists in completedWords, if not set its position equal to 1
                    await message.channel.send("Correct!")
                    await message.channel.send("You have " + str(tries) + " tries left") 
                    completedWords[check[1]] = 1 #TODO: Make it reprint the gameboard depending on how many words are left
                    if all(i == 1 for i in completedWords):
                        await message.channel.send("Congratulations! You did it!")
                        logic.Logic.endGame()
                        break
                else:
                    tries -= 1
                    await message.channel.send("You've already done this one")
                    await message.channel.send("You have " + str(tries) + " tries left") 
                    
            else:
              tries -= 1
              await message.channel.send("Wrong!")
              await message.channel.send("You have " + str(tries) + " tries left") 

            if (tries == 0):
                await message.channel.send("You lost! Loser stinky")
                logic.Logic.endGame()
                break

        if (not logic.Logic.inGame()):
            await message.channel.send("Use !play to start a game")
            


bot.run(config.token)