# TiniBot

### A Discord bot for the rest of us.

(name pending)

A Work in Progress Discord Bot with music, memery and miscellaneous functionality. This bot is in somewhat active development and hasn't reached a stable state just yet, so I'd not reccomend using it in your servers just yet, but hey, you do you.

## Commands

### Music

**!play**: Plays a music video searched on YouTube. You can also use a link! If the bot's already playing, the song will be automatically queued.

**!join**: Joins the voice call you're currently in.

**!volume**: Sets up the volume that the music will play in.

**!skip**: Votes to skip a song -- three votes are required to skip. The song requester can automatically skip.

**!volume**: Sets up the volume that the music will play in.

**!stop**: Clears the queue and leaves the voice channel.

**!playing**: Displays the song you're currently playing.

**!summon**: Summons the bot to join the current voice call you're in.

### Memery

*WIP*

### Misc

**!ping**: Returns a <<Pong!>> message. Pretty neat, huh?

**!say**: Say something -- the bot will say it back to you.

**!8ball**: Tini's also a fortune teller - ask something and she'll tell you the future!

**!commands**: Pops up a page somewhat similar to this. Sorta incomplete.

**!about**: You ever wanted to know everything about this bot? Here ya go, you silly doofus!

## Installation

0. Make sure you've got all of the dependencies. Get [Python](https://www.python.org/downloads/), [FFMPEG](https://www.ffmpeg.org/) and [YouTubeDL](https://rg3.github.io/youtube-dl/)(?). Install Discord.py by executing "python3 -m pip install -U discord.py[voice]" and install Pillow with "pip install pillow".

1. [Follow this page](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) on how to create a Discord Developer bot account and getting an unique token.

2. Download the ZIP file or clone the repo.

3. Edit bot.py, and at the end of the file change up the Discord bot.run("YOUR-TOKEN-HERE") for the token you got on the first step. Do the same on DMG.py.

4. (Optional) If you're on Windows, edit the location of the file on open.bat from c:\location\bot.py to where the bot files are located. This'll allow you to see errors when editing the file.

5. If you followed step 4, open the file *open.bat*. If not, open *bot.py*.

## Acknowledgements

[Discord Meme Generator, by Littlemansmg](https://github.com/Littlemansmg/Discord-Meme-Generator/blob/master/LICENSE)

[Music code, by YetiGuy!](https://www.youtube.com/watch?v=FpRzDY0-I1o)
