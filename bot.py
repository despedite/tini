import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import random
# Dependencies for Memery
from MemeFormatting import *
from datetime import datetime as dt
import asyncio
import logging
import os

startup_extensions = ["Music"]
bot = commands.Bot("!")

@bot.event
async def on_ready():
    print ("   ::::::::::::::::::::::::::    :::::::::::::::::::::::  ::::::::::::::::::: \n     :+:        :+:    :+:+:   :+:    :+:    :+:    :+::+:    :+:   :+:      \n    +:+        +:+    :+:+:+  +:+    +:+    +:+    +:++:+    +:+   +:+       \n   +#+        +#+    +#+ +:+ +#+    +#+    +#++:++#+ +#+    +:+   +#+        \n  +#+        +#+    +#+  +#+#+#    +#+    +#+    +#++#+    +#+   +#+         \n #+#        #+#    #+#   #+#+#    #+#    #+#    #+##+#    #+#   #+#          \n###    ##############    ########################  ########    ###           \n\nBot's online!")
    await bot.change_presence(game = discord.Game(name = "Torrenting self-awareness..."))

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

#soon(tm)

#@bot.event
#async def on_message(message):
#        if "eric" in message.content:
#                await bot.say("Es Erik con K, lameloide.")
        
#Deci: replica lo que acabas de decir.
@bot.command(pass_context=True)
async def say(ctx):
    msg = ctx.message.content.split(" ", 1)
    await client.delete_message(ctx.message)
    await client.send_message(ctx.message.channel, msg)
    
@bot.command(pass_context=True)
async def test(ctx, *msg):
    msg = ctx.message.content.split(" ", 1)
    if msg[1] == "yes":
        await bot.say("wow you did a thing")
    else:
        await bot.say("try !test yes")
    if len(msg) == 0:
        await bot.say("try an arg")

#Bola 8: frase al azar que predice el futuro. OOOooooOOOO. WIP: Hacer que no funcione sin un argumento.
@bot.command(name="8ball")
async def _8ball(ctx):
    items = ['here', 'It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Dont count on it.', 'My reply is no.', 'My sources say no', 'Outlook not so good.', 'Very doubtful.']
    await bot.say(random.choice(items))

#Ping, el comando obligatorio en todos los bots.
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong!")

#@bot.command(pass_context=True)
#async def revquotes(ctx):
    #revrng = ['_**I get off of school and this is what I see?**_', '_**OMFG, am I really that annoying? Dont answer that.**_', '_**SWIM WITH THE FISHES YOU SHINY METAL FUCK!**_', '_**And this concludes our episode of Math Fun with Northie and Friends. Tune in next time, kids!**_', '_**can we get some northie and friends fanart tho**_', '_**I wanna stroke my cock to anime cat girl pussies, omigod omigod omigod.**_', '_**IM GETTING FRIENDZONED BY A FUCKING ROBOT, MAN!**_', '_**Birthday is February 5th. Remember it or Ill incinerate you.**_', '_**Its not rape if theres heart in their eyes.**_', '_**Yeah, we have a fucking sex slave bot!**_', '_**As long as Onii-chan has dank memes, it doesnt matter.**_', '_**Hey, guys, Rev22360 here, and today we will be trying out Gizoogle.**_', '_**WHY ARE YOU SO SMOLL?**_', '_**Asians are art.**_', '_**And remember kids, eat your drugs, stay in vegetables, and dont do school.**_', '_**Id eat cake at any time of the day, but not the kind youre thinking of.**_', '_**Aw god, Im a trap!**_', '_**MOM, GET OUT OF MY ROOM, IM PLAYING MINECRAFT**_', '_**Im tryna get my dick wet by putting it in an asian pussy.**_', '_**Unless youre like me and you watch porn on your 3DS, then you have less to worry about.**_', '_**Dont try to keep up with the kids, man, its like, totally uncool.**_', '_**Hes a fatty fatty 2 by 4, cant get through the kitchen door.**_', '_**YOU MIGHT KNOW EVERYTHING IM GOING TO DO BUT THATS NOT GOING TO HELP YOU SINCE I KNOW EVERYTHING YOURE GOING TO DO! STRANGE ISNT IT!? GRRRRRRR!**_', '_**YOU CAN TAKE MY ASIANS! YOU CAN TAKE MY FRIENDS! BUT CAN NEVER TAKE MY FANS!!!**_', '_**Good Evening Twitter, this is your boy EatDatPussy445, and about like 30-45 minutes ago, I beat the fuck out of my dick so god damn hard that I cant even feel my left leg, my left leg has went totally numb. And, my dick has also went totally numb, to the point that it feels fucking weird when I go and take a piss.**_', '_**I love my fans!**_', '_**I?m gonna fuck your mother and burn your dog if you don?t kick that stupid bot.**_', '_**Aww yeah, I love asians.**_', '_**Can we get some fan-art coming up in here?**_', '_**The Multibit Hero: Corruption, coming soon 2026.**_', '_**Point is, you like a lot of hair.**_', '_**Yeah, which is why I nae-naed you.**_', '_**Eh, hes a Jake. Do it.**_', '_**Because no one wants to post their nudes in Velvet.**_', '_**Corner me against the wall, senpai! ~**_', '_**Well, at least I can get my hands on the damn sauce.**_', '_**I-Im not a weeb, b-baka! ~~**_', '_**TBH, the hair is pretty whack.**_', '_**!slapass**_', '_**Aww yeah.**_', '_**But I love Nadeko and Nadeko loves me!**_', '_**Subscribe to my YouTube channel.**_', '_**DAB!**_', '_**Incest, incest, its the best: put your sister to the test!**_', '_**I might be able to join. Depends on if my brother is gonna be a jackass as usual.**_', '_**Long Live RevBot3000.**_', '_**Im gonna fuck your mother and burn your dog if you don't kick that stupid bot.**_']
    #await bot.say(random.choice(revrng))
    
#Boludeces musicales, aparentemente.
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
            
#Comandos, usados con un embed. Pared de texto!
@bot.command(pass_context=True,name="commands")
async def _commands(ctx):
    embed = discord.Embed(colour=discord.Colour(0xaeb85d), description="**Music and Others**")
    embed.set_thumbnail(url="https://cdn2.iconfinder.com/data/icons/web-application-icons-part-i/100/Artboard_18-512.png")
    embed.set_author(name="Commands", icon_url="https://5.imimg.com/data5/RJ/XJ/MY-14679786/food-tin-can-500x500.png")
    embed.set_footer(text="Bot by @Erik#0911 - !about for more details", icon_url="https://media.discordapp.net/attachments/467845623807475714/470371819610963968/thegalherself.png?width=99&height=99")
    embed.add_field(name="!ping", value="Returns a <<Pong!>> message. Pretty neat, huh?")
    embed.add_field(name="!say", value="Say something -- the bot will say it back to you. Use !csay to get your message automatically deleted.")
    embed.add_field(name="!8ball", value="Did you know that I'm also a fortune teller? Ask me something and I'll tell you the future!")
    embed.add_field(name="!play", value="Plays a music video searched on YouTube. You can also use a link! If the bot's already playing, the song will be automatically queued.")
    embed.add_field(name="!join", value="Joins the voice call you're currently in.")
    embed.add_field(name="!volume", value="Sets up the volume that the music will play in.")
    embed.add_field(name="!skip", value="Votes to skip a song -- three votes are required to skip. The song requester can automatically skip.")
    embed.add_field(name="!volume", value="Sets up the volume that the music will play in.")
    embed.add_field(name="!stop", value="Clears the queue and leaves the voice channel.")
    embed.add_field(name="!playing", value="Displays the song you're currently playing.")
    embed.add_field(name="!summon", value="Summons the bot to join the current voice call you're in.")
    await bot.say(embed=embed)
    
#Acerca De, datos y boludeces.
@bot.command(pass_context=True)
async def about(ctx):
    embed = discord.Embed(colour=discord.Colour(0xaeb85d), description="**About the Bot**")
    embed.set_thumbnail(url="https://png.icons8.com/metro/1600/about.png")
    embed.set_author(name="Commands", icon_url="https://5.imimg.com/data5/RJ/XJ/MY-14679786/food-tin-can-500x500.png")
    embed.add_field(name="Bot created by @Erik#0911", value="Tini 0.1 - Not publically available on Github yet!")
    embed.add_field(name="Dependencies", value="Discord.py / FFMPEG / YoutubeDLL")
    embed.add_field(name="Acknowledgements", value="YetiGuy! on Youtube (Music code)")
    await bot.say(embed=embed)

# --------- Meme Generator -----------

logging.basicConfig(handlers = [logging.FileHandler('discord.log', 'a', 'utf-8')], level = logging.INFO)

toplist =[]
try:
    for root, dirs, files in os.walk("./Templates/Top"):
        for filename in files:
            name = filename.split('.')
            toplist.append(name[0])
except:
    pass
# memes that only use )top (top text only)
# toplist = ['mocking-spongebob']

# memes that only use )bottom (bottom text only)
bottomlist = []
try:
    for root, dirs, files in os.walk("./Templates/Bottom"):
        for filename in files:
            name = filename.split('.')
            bottomlist.append(name[0])
except:
    pass

topBottomList =[]
try:
    for root, dirs, files in os.walk("./Templates/TopAndBottom"):
        for filename in files:
            name = filename.split('.')
            topBottomList.append(name[0])
except:
    pass

# memes that use )top )bottom )tb
# topBottomList = [
#     '10-guy', 'bad-luck-brian', 'danger-zucc', 'good-guy-greg', 'roll-safe',
#     'simply', 'successkid', 'willy-wonka', 'zucc']

# ---------------------------HELP------------------------------------

listhelp = 'Prints a list of all the memes available.'

tbhelp = 'Prints top and bottom text memes.\n' \
         'Notes: This command can only be used with memes that are in the Top and Bottom List. ' \
         '\nTEXT MUST BE IN SINGLE OR DOUBLE QUOTES.\n' \
         'Example: )tb simply "One does not simply" "Program and not hate themselves"'

tophelp = 'Prints top text memes.\n' \
          'Notes: This command will only print toptext. It can only be used with memes that are in the Top List ' \
          'or Top and Bottom list.\n' \
          'Example: )top mocking-spongebob I\'m an example sentence'

bottomhelp = 'Prints bottom text memes.\n' \
             'Notes: This command will only print bottomtext. It can only be used with memes that are in the ' \
             'Bottom List or Top and Bottom list.\n' \
             'Example: )bottom roll-safe This isn\'t the correct format, but it works.'

suggesthelp = 'Sends a suggestion to the dev.\n' \
              'Notes: This command will send all suggestions to the developer of the bot. ' \
              'Feel free to suggest meme templates, features, or report any bugs here.\n' \
              'Example: )suggest Hey dev, get your shit together and add more memes.'

viewallhelp = 'Sends the user a template.\n' \
              'Notes: This command will PM the user a list of all available memes to choose from.\n' \
              'Example: )viewall '

viewallTop = 'Sends the user a template.\n' \
             'Notes: This command will PM the user a list of all available memes to choose from.\n' \
             'Example: )viewall top '

viewallTb = 'Sends the user a template.\n' \
            'Notes: This command will PM the user a list of all available memes to choose from.\n' \
            'Example: )viewall tb '

viewallBottom = 'Sends the user a template.\n' \
                'Notes: This command will PM the user a list of all available memes to choose from.\n' \
                'Example: )viewall bottom '

viewallMeme = 'Sends the user a template.\n' \
              'Notes: This command will PM the user a list of all available memes to choose from.\n ' \
              'Example: )viewall meme 10-guy '

devhelp = 'Provides notes and info from the dev.\n' \
          'Notes: This command is just to print out the dev\'s notes/thoughts.\n' \
          'Example: )dev'

# ---------------------------Logs------------------------------------

def commandInfo(ctx):
    now = dt.now().strftime('%m/%d %H:%M ')
    logging.info(now + ' Command Used: '
                 + ' Server: ' + ctx.message.server.name + ':' + ctx.message.server.id
                 + ' Author: ' + str(ctx.message.author)
                 + ' Invoke: \'' + str(ctx.message.content) + ' \'')

def commandWarning(ctx):
    now = dt.now().strftime('%m-%d_%H:%M:%S')
    logging.warning(now + ' Meme Missing.'
                    + ' Server: ' + ctx.message.server.name + ':' + ctx.message.server.id
                    + ' Author: ' + str(ctx.message.author)
                    + ' Invoke: \'' + str(ctx.message.content) + ' \'')

def commandCharLimit(ctx):
    now = dt.now().strftime('%m-%d_%H:%M:%S')
    logging.warning(now + ' Char limit reached.'
                    + ' Server: ' + ctx.message.server.name + ':' + ctx.message.server.id
                    + ' Author: ' + str(ctx.message.author)
                    + ' Invoke: \'' + str(ctx.message.content) + ' \'')

def masterWarning(ctx):
    now = dt.now().strftime('%m/%d %H:%M ')
    logging.info(now + ' Command Used: '
                 + ' Server: ' + ctx.message.server.name + ':' + ctx.message.server.id
                 + ' Author: ' + str(ctx.message.author)
                 + ' Invoke: \'' + str(ctx.message.content) + ' \'')

# ---------------------------Checks----------------------------------

def is_owner_check():
    def predicate(ctx):
        return ctx.message.author.id == '179050708908113920'
    return commands.check(predicate)

def maxChar(string):
    if len(string.strip()) > 35:
        raise commands.CheckFailure
    else:
        return

# ---------------------------BOT-------------------------------------

# execute if there is an error with a command.
@bot.event
async def on_command_error(error, ctx):
    # NOTE: It's stated in the documentation that CTX, should always be first.
    # for on_command_error, The first paramater is the error, and then the context
    # so error will always come first.

    if isinstance(error, commands.MissingRequiredArgument):
        # LOG
        now = dt.now().strftime('%m/%d %H:%M ')
        logging.error(now + str(error)
                      + ' Server: ' + ctx.message.server.name + ':' + ctx.message.server.id
                      + ' Author: ' + str(ctx.message.author)
                      + ' Invoke: \'' + str(ctx.message.content) + ' \'')

        # send error to discord.
        await bot.delete_message(ctx.message)
        await bot.say("You are missing some arguments.")

# Invoke: )tb <memetype> <topstring> <bottomstring>
@bot.command(pass_context=True, name='tb', description = "Prints top and bottom text.", help = tbhelp)
async def topAndBottom(ctx, memeType, topString, bottomString):
    # gets the channel the message from the context.
    destination = ctx.message.channel
    message = ctx.message

    # deletes message that invoked the command.
    await bot.delete_message(message)

    maxChar(topString)
    maxChar(bottomString)

    # check if in proper list
    if memeType in topBottomList:
        send = top_bottom(memeType, topString, bottomString)
        await bot.send_file(destination, send)
        # LOG
        commandInfo(ctx)

    # Warning
    else:
        await bot.say("Sorry, " + memeType + " isn't available or not in this list.")
        # LOG
        commandWarning(ctx)

@topAndBottom.error
async def topandbottom_error(error, ctx):
    if isinstance(error, commands.CheckFailure):
        await bot.say('Sorry. Only 35 characters allowed to keep the meme looking good.')
        # LOG
        commandCharLimit(ctx)

# Invoke: )top <memetype> <topstring>
@bot.command(pass_context = True, name = 'top',description = "Prints top text.", help = tophelp)
async def topText(ctx, memeType, *, topString):
    # gets the channel and the message from the context.
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    maxChar(topString)

    # check if in proper list
    if memeType in toplist:
        send = top_bottom(memeType, topString, '')
        await bot.send_file(destination, send)
        # LOG
        commandInfo(ctx)

    # check if in proper list
    elif memeType in topBottomList:
        send = top_bottom(memeType, topString, '')
        await bot.send_file(destination, send)
        # LOG
        commandInfo(ctx)

    # Warning
    else:
        await bot.say("Sorry, " + memeType + " isn't available or not in this list.")
        # LOG
        commandWarning(ctx)

@topText.error
async def topText_error(error, ctx):
    if isinstance(error, commands.CheckFailure):
        await bot.say('Sorry. Only 35 characters allowed to keep the meme looking good.')
        # LOG
        commandCharLimit(ctx)

# Invoke: )bottom <memetype> <bottomstring>
@bot.command(pass_context = True, name = 'bottom',description = "Prints bottom text.", help = bottomhelp)
async def bottomText(ctx, memeType, *, bottomString):
    # gets the channel and the message from the context.
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    maxChar(bottomString)

    # check if in proper list
    if memeType in toplist:
        send = top_bottom(memeType, '', bottomString)
        await bot.send_file(destination, send)
        # LOG
        commandInfo(ctx)

    # check if in proper list
    elif memeType in topBottomList:
        send = top_bottom(memeType, '', bottomString)
        await bot.send_file(destination, send)
        # LOG
        commandInfo(ctx)

    # Warning
    else:
        await bot.say("Sorry, " + memeType + " isn't available or not in this list.")
        # LOG
        commandWarning(ctx)

@bottomText.error
async def bottomText_error(error, ctx):
    if isinstance(error, commands.CheckFailure):
        await bot.say('Sorry. Only 35 characters allowed to keep the meme looking good.')
        # LOG
        commandCharLimit(ctx)

# Invoke: )list
@bot.command(pass_context = True, name = 'list', description = "Prints a list of memes.", help = listhelp)
async def listMemes(ctx):
    # gets the message from the context.
    message = ctx.message

    await bot.delete_message(message)

    # puts array's into a string form
    tmptop = ", ".join(toplist)
    tmpbottom = ", ".join(bottomlist)
    tmptb = ", ".join(topBottomList)

    await bot.say('```Top text only: ' + tmptop + '```')
    await bot.say('```Bottom text only: ' + tmpbottom + '```')
    await bot.say('```Top and Bottom text: ' + tmptb + '```')
    # LOG
    commandInfo(ctx)

# Invoke: )suggest <suggestion>
@bot.command(pass_context = True, name = 'suggest', description = "Sends the Bot Dev a suggestion.", help = suggesthelp)
async def suggest(ctx, *, suggestion):
    # gets the message from the context.
    message = ctx.message

    await bot.delete_message(message)

    # writes suggestion to a file
    with open('suggest.txt', 'a') as suggest:
        now = dt.now().strftime('%m/%d %H:%M ')
        suggest.write(now + " " + str(ctx.message.author) + ' Suggestion: ' + suggestion + "\n")

    await bot.say('Your suggestion has been recorded.')

    # Notifies specifically LittlemanSMG#6041 of any suggestion made
    owner = discord.utils.get(bot.get_all_members(), id = '179050708908113920')
    await bot.send_message(owner, 'Suggestion made. Check suggest.txt.')

    #LOG
    commandInfo(ctx)

# Invoke: )viewall
@bot.group(pass_context = True, name = 'viewall', description = "Display templates.", help = viewallhelp)
async def viewall(ctx):
    message = ctx.message

    await bot.delete_message(message)

    if ctx.invoked_subcommand is None:
        # send all memes to user via PM
        await bot.send_message(ctx.message.author, "Top and Bottom Text.")

        for tb in topBottomList:
            await bot.send_message(ctx.message.author, tb + ":")
            await bot.send_file(ctx.message.author, 'Templates/' + tb + '.jpg')

        await bot.send_message(ctx.message.author, "Top Text.")

        for top in toplist:
            await bot.send_message(ctx.message.author, top + ":")
            await bot.send_file(ctx.message.author, 'Templates/' + top + '.jpg')

        await bot.send_message(ctx.message.author, "Bottom Text.")

        for bottom in bottomlist:
            await bot.send_message(ctx.message.author, bottom + ":")
            await bot.send_file(ctx.message.author, 'Templates/' + bottom + '.jpg')

        #LOG
        commandInfo(ctx)

# Invoke )viewall top
@viewall.command(pass_context = True, name = 'top', help = viewallTop )
async def _top(ctx):
    # send all toplist memes to user via PM
    for meme in toplist:
        await bot.send_message(ctx.message.author, meme + ":")
        await bot.send_file(ctx.message.author, 'Templates/' + meme + '.jpg')

    #LOG
    commandInfo(ctx)

# Invoke )viewall tb
@viewall.command(pass_context = True, name = 'tb', help = viewallTb)
async def _tb(ctx):
    # send all topBottomlist memes to user via PM
    for meme in topBottomList:
        await bot.send_message(ctx.message.author, meme + ":")
        await bot.send_file(ctx.message.author, 'Templates/' + meme + '.jpg')

    #LOG
    commandInfo(ctx)

# Invoke )viewall bottom
@viewall.command(pass_context = True, name = 'bottom', help = viewallBottom)
async def _top(ctx):
    # send all bottomlist memes to user via PM
    for meme in bottomlist:
        await bot.send_message(ctx.message.author, meme + ":")
        await bot.send_file(ctx.message.author, 'Templates/' + meme + '.jpg')

    #LOG
    commandInfo(ctx)

# Invoke )viewall meme <meme>
@viewall.command(pass_context = True, name = 'meme', help = viewallMeme)
async def _view(ctx, meme):
    # send specific meme template to user via PM
    if meme in toplist or meme in topBottomList or meme in bottomlist:
        await bot.send_message(ctx.message.author, meme + ":")
        await bot.send_file(ctx.message.author, 'Templates/' + meme + '.jpg')
        # LOG
        commandInfo(ctx)

    else:
        await bot.send_message(ctx.message.author, "Can't find meme: " + meme)
        #LOG
        commandWarning(ctx)
# Invoke )dev
@bot.command(pass_context = True, name = 'dev', description = 'Prints dev notes', help = devhelp)
async def dev(ctx):
    # gets the message from the context.
    message = ctx.message

    await bot.delete_message(message)

    notes = '```' \
            'Author: Scott "LittlemanSMG" Goes.\n' \
            'Language: Python.\n\n' \
            'Notes about Generation-Meme: It only supports bottom and top text memes. This is because ' \
            'I\'m lazy and I need to learn how to format each meme. If you want to help, leave a' \
            'suggestion and I will get in contact with you.\n\n' \
            'Github: https://github.com/Littlemansmg/Discord-Meme-Generator \n\n' \
            'LOGGING: I\'m currently keeping logs of my bot usage. Log format goes as follows;\n' \
            '  <date> <server_name> <server_ID> <Username#0000> <command used>\n' \
            '```'
    await bot.say(notes)

# Invoke )master
@bot.command(pass_context = True, name = 'master', hidden = True)
@is_owner_check()
async def personalCommand(ctx, *, announcement):
    message = ctx.message

    await bot.delete_message(message)

    await bot.say('```' + announcement + '```')

@personalCommand.error
async def personalCommand_error(error, ctx):

    if isinstance(error, commands.CheckFailure):
        message = ctx.message

        await bot.delete_message(message)

        await bot.say("Fuck you. *How do you even know this command exists?*")
        masterWarning(ctx)

if __name__ == '__main__':
    if not os.path.exists('./Templates'):
        os.mkdir('./Templates')
        print('You don\'t have any templates!\n'
              'Don\'t worry, I took the liberty to make the "./Templates" folder.\n'
              'Add some images!')
        exit()

bot.run("BOT-TOKEN-HERE")