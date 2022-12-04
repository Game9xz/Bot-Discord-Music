import discord
from discord.utils import get
from discord import FFmpegPCMAudio
import youtube_dl
import asyncio
from async_timeout import timeout
from functools import partial
from discord.ext import commands
import itertools

bot = commands.Bot(command_prefix='/',help_command=None)

@bot.event
async def on_ready(): #ให้บอทออนไลน์
    print(f"Logged in as {bot.user}")

# intents = discord.Intents.default()
# intents.members = True
# client = discord.Client(intents = intents)

# @bot.event
# async def on_member_join(member):
#     guild = bot.get_guild(863331917704200192)
#     channel = guild.get_channel(863331917704200194)
#     emBed = discord.Embed(title = "ยินดีต้อนรับค่ะ 🙏",color = 0xf4e274, description = f"น้องเมดพร้อมรับใช้นายท่าน {member.mention} เเล้วค่ะ")
#     emBed.set_thumbnail(url = "https://www.img.in.th/images/e243ecaf243badf260112c6b904d523b.th.jpg")
#     await channel.send(embed= emBed)

# @bot.event
# async def on_member_remove(member):
#     guild = bot.get_guild(863331917704200192)
#     channel = guild.get_channel(863331917704200194)
#     emBed = discord.Embed(title = "ลาก่อนค่ะ 👋",color = 0xf4e274, description = f"{member.name} มีโอกาสไว้เจอกันใหม่นะคะ")
#     emBed.set_thumbnail(url = "https://www.img.in.th/images/bbe483a70a8ffcc153dc1221dbd142cf.th.jpg")
#     await bot.send_message(embed= emBed)

@bot.command() #บอกคำสั่งทั้งหมด
async def help(ctx): # คำสั่ง /help
    emBed = discord.Embed(title="คำสั่งเมด", description="รวบรวมคำสั่งทั้งหมดไว้เพื่อนายท่านที่น่ารัก", color=0xFE6F5E)
    emBed.add_field(name="/help", value="คำสั่งเมดทั้งหมด", inline="False")
    emBed.add_field(name="/music", value="คำสั่งเมดร้องเพลงทั้งหมด", inline="False")
    emBed.add_field(name="/hello", value="ทักทายนายท่านของหนู", inline="False")
    emBed.add_field(name="/say", value="นายท่านอยากให้หนูพูดว่าอะไรคะ", inline="False")
    emBed.add_field(name="/leave", value="พาหนูออกจากห้อง", inline="False")
    emBed.set_thumbnail(url='https://www.img.in.th/images/f73877a36eb531f6bbc65b1fa381984e.th.jpg')
    emBed.set_footer(text="M4ID", icon_url='https://www.img.in.th/images/3ab51c65d5193ae1d017bc01ac582f77.th.jpg')
    await ctx.channel.send(embed=emBed)

@bot.command() #บอกคำสั่งเล่นเพลงทั้งหมด
async def music(ctx): # คำสั่ง /music
    emBed = discord.Embed(title="คำสั่งร้องเพลง", description="รวบรวมคำสั่งทั้งหมดไว้เพื่อนายท่านที่น่ารัก", color=0xc48bd0)
    emBed.add_field(name="/p", value="น้องเมดร้องเพลง", inline="False")
    emBed.add_field(name="/stop", value="หยุดเพลงถาวร", inline="False")
    emBed.add_field(name="/pause", value="หยุดเพลงชั่วคราว", inline="False")
    emBed.add_field(name="/resume", value="เริ่มเพลง", inline="False")
    emBed.add_field(name="/skip", value="ข้ามเพลง", inline="False")
    emBed.add_field(name="/queue", value="คิวเพลง", inline="False")
    emBed.set_thumbnail(url='https://www.img.in.th/images/08f5e28f225bd96b286d05348ae3bce3.th.jpg')
    emBed.set_footer(text="M4ID", icon_url='https://www.img.in.th/images/df9ccdb9f54e90732005730b9f92b5cf.th.jpg')
    await ctx.channel.send(embed=emBed)

@bot.command()
async def say(ctx, *, par): # คำสั่ง /say
    await ctx.channel.send("นายท่านสั่งให้หนูพูดว่า {0}".format(par))

@bot.event #ให้น้องตอบกลับ
async def on_message(message):
    if message.content == '/hello':
        await message.channel.send('สวัสดีค่ะนายท่าน ' + str(message.author.name) + ' หนูชื่อ ' + str(bot.user.name) + ' เป็นน้องเมดประจำที่นี่ ยินดีที่ได้รู้จักค่ะ 😊')
    elif message.content == 'สวัสดี':
        await message.channel.send('สวัสดีค่ะนายท่าน ' + str(message.author.name))
    elif message.content == 'สวัสดีค่ะ':
        await message.channel.send('สวัสดีค่ะนายท่าน ' + str(message.author.name))
    elif message.content == 'สวัสดีครับ':
        await message.channel.send('สวัสดีค่ะนายท่าน ' + str(message.author.name))
    elif message.content == 'สวัสดีงับ':
        await message.channel.send('สวัสดีค่ะนายท่าน ' + str(message.author.name))
    elif message.content == 'สวัสดีค้าบ':
        await message.channel.send('สวัสดีค่ะนายท่าน ' + str(message.author.name))
    elif message.content == 'สวัสดีน้องเมด':
        await message.channel.send('สวัสดีค่ะนายท่าน ' + str(message.author.name))

    elif message.content == 'ง่างื้อ':
        await message.channel.send('ง่างื้อพ่อง!')
    elif message.content == 'อุเเงง':
        await message.channel.send('ไม่ร้องนะคะ 🥺')
    elif message.content == 'เเงง':
        await message.channel.send('ไม่ร้องนะคะ 🥺')
    elif message.content == 'รักนะ':
        await message.channel.send('รักนายท่าน ' + str(message.author.name) + ' เหมือนกันค่ะ 😘')
    elif message.content == '/exit':
        await bot.logout()
    await bot.process_commands(message)

##############################################################

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn',
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5" ## song will end if no this line
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        """Allows us to access attributes similar to a dict.
        This is only useful when you are NOT downloading.
        """
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        await ctx.send(f'```ini\n[✅ เพิ่มเพลง {data["title"]} ไว้ในคิว]\n```') #delete after can be added

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source, **ffmpeg_options), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        """Used for preparing a stream, instead of downloading.
        Since Youtube Streaming links expire."""
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url'], **ffmpeg_options), data=data, requester=requester)

class MusicPlayer:
    """A class which is assigned to each guild using the bot for Music.
    This class implements a queue and loop, which allows for different guilds to listen to different playlists
    simultaneously.
    When the bot disconnects from the Voice it's instance will be destroyed.
    """

    __slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current', 'np', 'volume')

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog

        self.queue = asyncio.Queue()
        self.next = asyncio.Event()

        self.np = None  # Now playing message
        self.volume = .5
        self.current = None

        ctx.bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        """Our main player loop."""
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            try:
                # Wait for the next song. If we timeout cancel the player and disconnect...
                async with timeout(300):  # 5 minutes...
                    source = await self.queue.get()
            except asyncio.TimeoutError:
                del players[self._guild]
                return await self.destroy(self._guild)

            if not isinstance(source, YTDLSource):
                # Source was probably a stream (not downloaded)
                # So we should regather to prevent stream expiration
                try:
                    source = await YTDLSource.regather_stream(source, loop=self.bot.loop)
                except Exception as e:
                    await self._channel.send(f'❌ เกิดข้อผิดพลาดในการประมวลผลเพลง\n'
                                             f'```css\n[{e}]\n```')
                    continue

            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            self.np = await self._channel.send(f'**🔊 กำลังเล่นเพลง : ** `{source.title}` เปิดโดยนายท่าน '
                                               f'`{source.requester}`')
            await self.next.wait()

            # Make sure the FFmpeg process is cleaned up.
            source.cleanup()
            self.current = None

            try:
                # We are no longer playing this song...
                await self.np.delete()
            except discord.HTTPException:
                pass

    async def destroy(self, guild):
        """Disconnect and cleanup the player."""
        del players[self._guild]
        await self._guild.voice_client.disconnect()
        return self.bot.loop.create_task(self._cog.cleanup(guild))

#######################################################################

@bot.command() #เพลง
async def p(ctx,* , search: str ) : #เล่นเพลง
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients,guild = ctx.guild)

    if voice_client == None:
        await ctx.channel.send("🎤 น้องเมดเริ่มร้องเพลง!")
        await channel.connect()
        voice_client = get(bot.voice_clients,guild = ctx.guild)
    await ctx.trigger_typing()

    _player = get_player(ctx)
    source = await YTDLSource.create_source(ctx, search, loop = bot.loop, download = False)
    await _player.queue.put(source)

players = {}
def get_player(ctx):
    try:
        player = players[ctx.guild.id]
    except:
        player = MusicPlayer(ctx)
        players[ctx.guild.id] = player
    return player

@bot.command() #หยุดเพลงถาวร
async def stop(ctx):
    voice_client = get(bot.voice_clients,guild = ctx.guild)
    if voice_client == None:
        await ctx.channel.send("หยุดเพลง")
        return
    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("📢 น้องเมดอยู่ห้อง {0}".format(voice_client.channel) + " ไม่สามารถหยุดเพลงได้!")
        return
    voice_client.stop()

@bot.command() #หยุดเพลงชั่วคราว
async def pause(ctx):
    voice_client = get(bot.voice_clients,guild = ctx.guild)
    if voice_client == None:
        await ctx.channel.send("หยุดเพลง")
        return
    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("📢 น้องเมดอยู่ห้อง {0}".format(voice_client.channel) + " ไม่สามารถหยุดเพลงชั่วคราวได้!")
        return
    voice_client.pause()

@bot.command() #เริ่มเพลงเดิม
async def resume(ctx):
    voice_client = get(bot.voice_clients,guild = ctx.guild)
    if voice_client == None:
        await ctx.channel.send("เริ่มเพลง")
        return
    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("📢 น้องเมดอยู่ห้อง {0}".format(voice_client.channel) + " ไม่สามารถเริ่มเพลงได้!")
        return
    voice_client.resume()

@bot.command()
async def queue(ctx):
    voice_client = get(bot.voice_clients, guild = ctx.guild)
    if voice_client == None or not voice_client.is_connected():
        await ctx.channel.send("คิวเพลง", delete_after = 10)
        return
    player = get_player(ctx)
    if player.queue.empty():
        return await ctx.send('❌ ไม่มีเพลงในคิว')
    
    upcoming = list(itertools.islice(player.queue._queue,0,player.queue.qsize()))
    fmt = '\n'.join(f'**`{_["title"]}`**' for _ in upcoming)
    embed = discord.Embed(title = f'เพลงในคิว {len(upcoming)} เพลง', description = fmt)
    await ctx.send(embed = embed)

@bot.command() #ข้ามเพลง
async def skip(ctx):
    voice_client = get(bot.voice_clients, guild = ctx.guild)
    if voice_client == None or not voice_client.is_connected():
        await ctx.channel.send("ข้ามเพลง", delete_after = 10)
        return
    if voice_client.is_paused():
        pass
    elif not voice_client.is_playing():
        return
    voice_client.stop()
    await ctx.send(f'**`{ctx.author}`** : ข้ามเพลง!')

@bot.command() #เอาบอทออก
async def leave(ctx):
    del players[ctx.guild.id]
    await ctx.voice_client.disconnect()


bot.run('#')