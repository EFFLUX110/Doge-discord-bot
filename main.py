import discord
import asyncio
from discord_components import *
from textblob import TextBlob
from discord.ext.commands import bot
from discord.utils import get
from discord.ext import commands, tasks
from GoogleNews import GoogleNews
googlenews=GoogleNews()
googlenews=GoogleNews('en')
import os
import requests
import json
import time
import random
import datetime
import pyjokes

intents = discord.Intents.default()
intents.members = True
intents = intents.all()

client=commands.Bot(command_prefix="%", intents=intents)

client.remove_command('help')
status=['cooking code','eating logic','%help']

@client.event
async def on_ready():
  change_status.start()
  meme1.start()
  DiscordComponents(client)
  print("we have logged in as {0.user}".format(client))

@tasks.loop(seconds=2)
async def change_status():
  await client.change_presence(activity=discord.Game(random.choice(status)))

@tasks.loop(seconds=7200)
async def meme1():
  c=int(here your channel id will be there, in which auto meme will be posted after every 2 hrs)
  channel1 = client.get_channel(c)
  r=requests.get("https://memes.blademaker.tv/api?lang=en")
  res=r.json()
  title=res['title']
  ups=res['ups']
  downs=res['downs']
  sub=res['subreddit']
  m=discord.Embed(title=f"{title}\nsubreddit: {sub}")
  m.set_image(url=res["image"])
  m.set_footer(text="Automatic meme for your server")
  await channel1.send(embed=m)

@client.command()
async def hello(ctx):
  await ctx.send('hey! I am doge, type %help to see what can I do hue hue !!')

@client.command()
async def meme(ctx):
  r=requests.get("https://memes.blademaker.tv/api?lang=en")
  res=r.json()
  title=res['title']
  ups=res['ups']
  downs=res['downs']
  sub=res['subreddit']
  m=discord.Embed(title=f"{title}\nsubreddit: {sub}")
  m.set_image(url=res["image"])
  m.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=m)

@client.command()
async def server(ctx):
  name=str(ctx.guild.name)
  region=str(ctx.guild.region)
  owner=str(ctx.guild.owner)
  id=str(ctx.guild.id)
  MemberCount = str(ctx.guild.member_count)
  icon=str(ctx.guild.icon_url)

  embed=discord.Embed(
    title=name+' Server Information',
    colour=discord.Color.green()
  )
  embed.set_thumbnail(url=icon)
  embed.add_field(name='Owner',value=owner,inline=True)
  embed.add_field(name='Server ID',value=id,inline=True)
  embed.add_field(name='Region',value=region,inline=True)
  embed.add_field(name='Member Count',value=MemberCount,inline=True)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

@client.event
async def on_member_join(member):
    Count = str(member.guild.member_count)
    description=str(member.guild.description)
    icon=str(member.guild.icon_url)
    embed = discord.Embed(title=f'welcome {member.name} !\nwelcome to {member.guild.name} you are currently the {Count}th member ',color=0x0061ff,font_size=200)
    embed.set_thumbnail(url=icon)
    embed.add_field(name='Description',value=description)
    u=int(here your channel id will be there where bot will send welcome msg)
    if member.guild.name == 'Test':     #instead of Test you have to write your server name
      await client.get_channel(u).send(embed=embed)
@client.event
async def on_message_delete(message):
    if len(message.mentions) == 0:
        return
    else:
        ghostping = discord.Embed(title=f'GHOSTPING CAUGHT', color=0xe74c3c, timestamp=message.created_at)
        ghostping.add_field(name='**Name:**', value=f'{message.author} ({message.author.id})')
        ghostping.add_field(name='**Message:**', value=f'{message.content}')
        ghostping.set_thumbnail(
            url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXtzZMvleC8FG1ExS4PyhFUm9kS4BGVlsTYw&usqp=CAU')
        try:
            await message.channel.send(embed=ghostping)
        except discord.Forbidden:
            try:
                await message.author.send(embed=ghostping)
            except discord.Forbidden:
                return

@client.command()
async def analyze(ctx):
  await ctx.reply('write a paragraph or a lengthy line...')
  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel
  msg = await client.wait_for("message", check=check)
  text=msg.content
  blob=TextBlob(text)
  sentiment=blob.sentiment.polarity
  if sentiment>0:
    await msg.reply(f'I think this is positve , positivity lvl:{sentiment}')
  else:
    await msg.reply(f'I think this is  negavtive , negavtivity lvl:{sentiment}')
   
@client.command()
async def analyze_channel(ctx,channel: discord.TextChannel):
  ooo=int(channel.id)
  channel = client.get_channel(ooo)
  messages = await ctx.channel.history(limit=500).flatten()
  k=""
  for msg_ch in messages:
    an=k+' '+msg_ch.content
    k=an
  blob=TextBlob(k)
  sentiment=blob.sentiment.polarity
  if sentiment>0:
    await ctx.reply(f'I have analyzed last 500 chats and I think your members r happy :), positivity lvl:{sentiment}')
  elif sentiment==0:
    await ctx.reply(f"I have analyzed last 500 chats and I think your members' feeling is neutral")
  else:
    await ctx.reply(f"I have analyzed last 500 chats and I think your members r not happy :(, negavtivity lvl:{sentiment}")

@client.command()
async def insta_caption(ctx):
  response=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote =json_data[0]['q']
  await ctx.send(quote)
@client.command()
async def jokes(ctx):
  joke=pyjokes.get_joke()
  await ctx.send(joke)
@client.command()
async def hack(ctx):
  n=random.randint(0,1)
  if n==0:
    a1='RUBBER DUCKY SCRIPT STARTED'
    b1='▒▓█►─═bypassed discord═─◄█▓▒'
    c1='█►─═injecting ransomware malware═─◄█'
    d1='[:]accesing root directory'
    e1='[..]formating system'
    f1='[:]hacking nasa'
    g1='[..]hacking nasa started'
    h1='[:]nasa database fenching finished'
    i1='[..]performing DDoS attack'
    j1='[:]Selling sensitive details on dark web'
    k1="[..]removing attacker's name from fbi list"
    l1='[:]hacked the target succesfully'
    m1='[..]here is a candy 🍬 left for the victim :)'  
    message=await ctx.reply('your hacking script loaded')
    time.sleep(2)
    z=await message.edit(content='<-------------------------')
    time.sleep(0.1)
    z=await message.edit(content='.    <--------------------')
    time.sleep(0.1)
    z=await message.edit(content='.         <---------------')
    time.sleep(0.1)
    z=await message.edit(content='.               <---------')
    time.sleep(0.1) 
    z=await message.edit(content='.                    <----')
    time.sleep(0.1)
    z=await message.edit(content='.                      <--')
    time.sleep(0.1)
    z=await message.edit(content='.                        <')
    time.sleep(0.1)
    await message.edit(content=a1)
    time.sleep(1)
    await message.edit(content=b1)
    time.sleep(2)
    await message.edit(content=c1)
    time.sleep(2)
    await message.edit(content=d1)
    time.sleep(2)
    await message.edit(content=e1)
    time.sleep(2)
    await message.edit(content=f1)
    time.sleep(2)
    await message.edit(content=g1)
    time.sleep(2)
    await message.edit(content=h1)
    time.sleep(2)
    await message.edit(content=i1)
    time.sleep(2)
    await message.edit(content=j1)
    time.sleep(2)
    await message.edit(content=k1)
    time.sleep(2)
    await message.edit(content=l1)
    time.sleep(2)
    await message.edit(content=m1)
    time.sleep(2)
  else:
    z=await ctx.reply('BLINK!!')
    time.sleep(1)
    await z.delete()
    z=await ctx.send('BLINK!!')
    time.sleep(1)
    await z.delete()
    z=await ctx.send('BLINK!!')
    time.sleep(1)
    await z.delete()
    z=await ctx.send('SCRIPT CRASHED')
    time.sleep(1)
    x='ERROR IN FENCHING DETAILS'
    time.sleep(2)
    await z.edit(content=x)
    x='UNFORTUNATELY'
    time.sleep(2)
    await z.edit(content=x)
    x='THE MEMBER YOU WERE GOING TO HACK IS A MEMBER OF ANONNYMOUS'
    time.sleep(3)
    await z.edit(content=x)
    x='BETTER LUCK NEXT TIME'
    time.sleep(2)
    await z.edit(content=x)

@client.command()
async def giveaway(ctx, mins:int,*,prize:str):
  embed =discord.Embed(title="GIVEAWAY PRIZES",description=f"{prize}",color=ctx.author.color)
  ends = datetime.datetime.utcnow()+datetime.timedelta(seconds= mins*60)
  embed.add_field(name="ENDING AT: ",value=f"{ends} UTC")
  embed.set_image(url='https://media.giphy.com/media/R9YeL5bxPc34c/giphy.gif')
  embed.set_thumbnail(url='https://media.giphy.com/media/mnFNB5IIabdgVve3zb/giphy.gif')
  embed.set_footer(text=f"ends {mins} minutes from now!!!")
  embed.set_footer(text=f"THIS IS JUST FOR FUN , DONT GO TO ASK UR ADMIN ABOUT THE PRIZES LOL😂 Requested by {ctx.author}")

  h=await ctx.send(embed=embed)
  await h.add_reaction('🥳')
  await asyncio.sleep(mins)
  new_h=await ctx.channel.fetch_message(h.id)
  users=await new_h.reactions[0].users().flatten()
  users.pop(users.index(client.user))
  winner=random.choice(users)
  await ctx.send(f"congratulations! {winner.mention} won {prize} in his/her imagination🤩")

@client.command()
async def inspire(ctx):
  response=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote =json_data[0]['q'] + " -"+json_data[0]["a"]
  await ctx.send(quote)

@client.command()
async def help(ctx):
  Fun=['**%hack\n**:> become a black hat pro lvl hacker\n', '**%meme\n**:> get a random meme\n','**%jokes** \n:> Bored ???\n','**%server**\n:> server information\n','**%inspire**\n:> need some inspiration ??\n','**%insta_caption**\n:> what will you write in ur next post?\n', '**%giveaway**\n:> start spreading gifts\n']

  Game=['**%rps\n**:> play Rock Paper Scissors\n','**%guess\n**:> Can you guess which colour is it ?\n','**%amongus\n**:> shhhhhhhhh!\n','**%football\n**:> want to make a goal ??']
  Crypto=['**%top\n**:> Top four trending cryptocurrency\n']
  Info=['**%hello\n**:> Say hello to me\n','**%ping\n**:> check latency\n','**%invite\n**:> Can I join your server please ?\n','**%analyze\n**:> Let me analyze whether it is positve or negavtive comment ?\n','**%analyze_channel #mention\n**:> Let me analyze whether your server members r happy or not \n']

  hel=discord.Embed(title='LIST OF COMMANDS', description ="Click anyone to explore",color=0x3498db)
  hel.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  game=discord.Embed(title='Games', description =''.join(Game),color=0x3498db)
  game.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  fun=discord.Embed(title='Fun', description =''.join(Fun),color=0x3498db)
  fun.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  crypto=discord.Embed(title='crypto', description =''.join(Crypto),color=0x3498db)
  crypto.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  info=discord.Embed(title='Info', description =''.join(Info),color=0x3498db)
  info.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  cha=discord.Embed(title='Succesfull Click',color=0x3498db)

  m = await ctx.reply(
        embed=hel,
        components=[[Button(style=1, label="Games"),Button(style=3, label="Fun"),Button(style=ButtonStyle.red,label="Crypto"),Button(style=ButtonStyle.grey,label="Info")]
        ],
    )
  def check(res):
    return ctx.author == res.user and res.channel == ctx.channel
  
  res = await client.wait_for("button_click", check=check)
  if res.component.label=="Games":
    cha=discord.Embed(title='Succesfull Click',description="Click %help to load again",color=0x3498db)
    cha.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    await m.edit(embed=cha, components=[[Button(style=1, label="Games"),Button(style=3, label="Fun"),Button(style=ButtonStyle.red,label="Crypto"),Button(style=ButtonStyle.grey,label="Info")]],)
   
    await ctx.send(embed=game,components=[],)

  if res.component.label=="Fun":
    await m.edit(embed=cha, components=[],)
    await ctx.send(embed=fun, components=[],)
  if res.component.label=="Crypto":
    await m.edit(embed=cha, components=[],)
    await ctx.send(embed=crypto, components=[],)
  if res.component.label=="Info":
    await m.edit(embed=cha, components=[],)
    await ctx.send(embed=info, components=[],)

@client.command()
async def top(ctx):
  await ctx.reply("please wait ...")
  from bs4 import BeautifulSoup
  import requests
  def GETC():
    url=f'https://www.google.com/search?q=bitcoin+price'
    HTML=requests.get(url)
    soup=BeautifulSoup(HTML.text,'html.parser')
    text=soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    return text
  def bitC():
    url=f'https://www.google.com/search?q=bitcoin cash+price'
    HTML=requests.get(url)
    soup=BeautifulSoup(HTML.text,'html.parser')
    text=soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    return text
  def LITE():
    url=f'https://www.google.com/search?q=litecoin+price'
    HTML=requests.get(url)
    soup=BeautifulSoup(HTML.text,'html.parser')
    text=soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    return text
  def ETH():
    url=f'https://www.google.com/search?q=ethereum+price'
    HTML=requests.get(url)
    soup=BeautifulSoup(HTML.text,'html.parser')
    text=soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    return text
  bit=GETC()
  lite=LITE()
  eth=ETH()
  bitca=bitC()
  e = discord.Embed(title="cryptocurrency", description="Click anyone to see",color=0x3498db)
  Bitcoin=discord.Embed(title='BITCOIN PRICE', description =bit,color=0x3498db)
  bitcoin_cash=discord.Embed(title='Bitcoin cash PRICE', description =bitca,color=0x3498db)
  Litcoin=discord.Embed(title='LITECOIN PRICE', description =lite,color=0x3498db)
  Ethereum=discord.Embed(title='ETHEREUM PRICE', description =eth,color=0x3498db)
  m = await ctx.reply(
        embed=e,
        components=[[Button(style=1, label="Bitcoin"),Button(style=3, label="bitcoin cash"),Button(style=ButtonStyle.red,label="Litecoin"),Button(style=ButtonStyle.grey,label="Ethereum")]
        ],
    )
  def check(res):
        return ctx.author == res.user and res.channel == ctx.channel
  res = await client.wait_for("button_click", check=check)
  if res.component.label=="Bitcoin":
    await ctx.send(embed=Bitcoin, components=[],)
  if res.component.label=="bitcoin_cash":
    await ctx.send(embed=bitcoin_cash, components=[],)
  if res.component.label=="Ethereum":
    await ctx.send(embed=Ethereum, components=[],)
  if res.component.label=="Litcoin":
    await ctx.send(embed=Litcoin, components=[],)

@client.command()
async def amongus(ctx):
    e = discord.Embed(title=f"{ctx.author}'s' amongus Game!", description="> Kill the imposter fast! <",color=0x3498db)
    
    e1 = discord.Embed(title=f"{ctx.author}, You Guessed It Right!", description="> You have won! <",color=0x00FF00)
    
    e3 = discord.Embed(title=f"{ctx.author}, You didn't Click on Time", description="> Timed Out! <",color=discord.Color.red())

    e2 = discord.Embed(title=f"{ctx.author}, You Lost!", description="> You have lost! <",color=discord.Color.red())
      
    m = await ctx.reply(
        embed=e,
        components=[[Button(style=1, label="Blue ඞ"),Button(style=3, label="Green ඞ"),Button(style=ButtonStyle.red,label="Red ඞ"),Button(style=ButtonStyle.grey,label="grey ඞ")]
        ],
    )

    def check(res):
      return ctx.author == res.user and res.channel == ctx.channel

    try:
      res = await client.wait_for("button_click", check=check, timeout=5)
      ch=['Blue ඞ','Green ඞ','Red ඞ','grey ඞ']
      if res.component.label==random.choice(ch):
        
        await m.edit(embed=e1,components=[],)
      else: 
        await m.edit(embed=e2, components=[],)
    except asyncio.TimeoutError:
      await m.edit(
          embed=e3,
          components=[],
      )

@client.command()
async def guess(ctx):
    e = discord.Embed(title=f"{ctx.author}'s' Guessing Game!", description="> Click a button to choose! <",color=0x3498db)
    
    e1 = discord.Embed(title=f"{ctx.author}, You Guessed It Right!", description="> You have won! <",color=0x00FF00)
    
    e3 = discord.Embed(title=f"{ctx.author}, You didn't Click on Time", description="> Timed Out! <",color=discord.Color.red())

    
    e2 = discord.Embed(title=f"{ctx.author}, You Lost!", description="> You have lost! <",color=discord.Color.red())
  
    
    m = await ctx.reply(
        embed=e,
        components=[[Button(style=1, label="Blue"),Button(style=3, label="Green"),Button(style=ButtonStyle.red,label="Red")]
        ],
    )

    def check(res):
        return ctx.author == res.user and res.channel == ctx.channel

    try:
        res = await client.wait_for("button_click", check=check, timeout=5)
        ch=['Blue','Green','Red']
        if res.component.label==random.choice(ch):
          
          await m.edit(embed=e1,components=[],)
        else: 
          await m.edit(embed=e2, components=[],)
          

    except asyncio.TimeoutError:
        await m.edit(
            embed=e3,
            components=[],
        )

@client.command()
async def rps(ctx):
    ch1 = ["Rock","Scissors","Paper"]
    comp = random.choice(ch1)
  
    yet = discord.Embed(title=f"{ctx.author.display_name}'s ROCK PAPER SCISSORS Game",description=">status: Waiting for a click , 5 sec left" )
    
    win = discord.Embed(title=f"{ctx.author.display_name}, You won!",description=f">status: You Won -- Bot had chosen {comp}")
    
    out = discord.Embed(title=f"{ctx.author.display_name}' You didn't click on time",description=">status: Time Out!!")
    
    lost = discord.Embed(title=f"{ctx.author.display_name}You lost the Game",description=f">status: bot had chosen {comp}")
  
    tie = discord.Embed(title=f"{ctx.author.display_name} Game Tie>",description=">status: It was tie")
       
    m = await ctx.reply(
        embed=yet,
        components=[[Button(style=1, label="Rock",emoji="💎"),Button(style=3, label="Paper",emoji="📝"),Button(style=ButtonStyle.red, label="Scissors",emoji="✂️")]
        ],
    )

    def check(res):
        return ctx.author == res.user and res.channel == ctx.channel

    try:
      res = await client.wait_for("button_click", check=check, timeout=7)
      player = res.component.label
      
      if player==comp:
        await m.edit(embed=tie,components=[])
        
      if player=="Rock" and comp=="Paper":
        await m.edit(embed=lost,components=[])
        
      if player=="Rock" and comp=="Scissors":
        await m.edit(embed=win,components=[])
       
      if player=="Paper" and comp=="Rock":
        await m.edit(embed=win,components=[])
        
      if player=="Paper" and comp=="Scissors":
        await m.edit(embed=lost,components=[])
        
      if player=="Scissors" and comp=="Rock":
        await m.edit(embed=lost,components=[])
        
      if player=="Scissors" and comp=="Paper":
        await m.edit(embed=win,components=[])
      
    except asyncio.TimeoutError:
      await m.edit(
          embed=out,
          components=[],
      )

@client.command()
async def football(ctx):
  options=["LEFT",'MIDDLE','RIGHT']
  computerOption = random.choice(options)
  def goal():
    if computerOption=='LEFT':
        return('.🧍‍♂️')
    if computerOption=='MIDDLE':
        return ('⁃⁃⁃⁃⁃⁃🧍‍♂️')
    if computerOption=='RIGHT':
        return ('⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃🧍‍♂️')

  yet = discord.Embed(title=f"{ctx.author.display_name}'s PENALTY SHOOTOUT GAME",description=">status: Waiting for a click , 5 sec left" )
  yet.add_field(name=".🥅    🥅    🥅", value=goal() , inline=False)
  out = discord.Embed(title=f"{ctx.author.display_name}' You didn't click on time",description=">status: Time Out!!")
  win = discord.Embed(title=f"{ctx.author.display_name}, congratulations!",description="GOOOOOAL !!!!")
  miss = discord.Embed(title="MISSED !!",description="Keeper dived")
  save = discord.Embed(title="SAVED !!",description="Keeper saved")

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel

  m = await ctx.reply(
        embed=yet,
        components=[[Button(style=1, label="LEFT",emoji="⚽"),Button(style=3, label="MIDDLE",emoji="⚽"),Button(style=ButtonStyle.red, label="RIGHT",emoji="⚽")]
        ],
    )
  missChance=random.randint(1,2)
  try:
    res = await client.wait_for("button_click", check=check, timeout=7)
    shoot = res.component.label
    if shoot == computerOption :
      await m.edit(embed=save,components=[])
    elif missChance == 1:
      await m.edit(embed=miss,components=[])
    else :
      await m.edit(embed=win,components=[])

  except TimeoutError:
    await m.edit(
          embed=out,
          components=[],
      )

@client.command()
async def invite(ctx):
  embed=discord.Embed(color=0x00FFFF)
  await ctx.send('🤖BOT url',components=[Button(style=5,url='https://discord.com/api/oauth2/authorize?client_id=836193148861677568&permissions=2148006977&scope=bot',label='EFFLUX')])
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    embed = discord.Embed(
        title='EFFLUX Bot Latency',
        description="Latency",
        color=0x00FFFF)
    embed.add_field(name="🤖BOT Latency",value=f"{str(round(client.latency * 1000))}ms", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


client.run('Here your key will be there')

