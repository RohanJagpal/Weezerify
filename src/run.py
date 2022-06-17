import discord
from dotenv import load_dotenv
import os
from time import sleep

client = discord.Client(activity=discord.Game(name='Buddy Holly!'))
load_dotenv()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_voice_state_update(member, before, after):
    if not member.id == 302471371319934997:
        return
    if member.voice and not member.guild.voice_client:
        vc = await member.voice.channel.connect()
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=member.guild)
        if not voice_client.is_playing():
            vc.play(discord.FFmpegPCMAudio(executable="./bin/ffmpeg.exe", source="./src/Buddy_Holly_But_Its_Just_The_Guita_(getmp3.pro).mp3"))
            while vc.is_playing():
                sleep(.1)
            sleep(1)
            await vc.disconnect()

client.run(os.getenv("DISCORD_TOKEN"))