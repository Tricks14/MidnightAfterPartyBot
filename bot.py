import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='N',description='This bot is made by Tricks using Python')

users = (len(set(bot.get_all_members())))

bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(discord.__version__)
    users = sum(1 for _ in bot.get_all_members())
    await bot.change_presence(game=discord.Game(name='With {} users, PREFIX=N'.format(users)))
    
@bot.command()
async def botspurpose(ctx):
    await ctx.send("This bot is made for Midnight After Party")
    
@bot.command()
async def botowner(ctx):
    await ctx.send("<@188614474167484416> is owner of this bot")
    
@bot.command()
async def serverinv(ctx):
    await ctx.send("https://discord.gg/TzukCVr")
    
@bot.command()
async def partnerinfo(ctx):
    await ctx.send("""```:christmas_tree: **Welcome to Midnight AfterParty** :christmas_tree: 
__About us:__ @everyone
:tickets: **1900+ Members!**
:fireworks: **Experienced StaffTeam**
:fire: **Active Staffs!**
:tickets: **Friendly members!**
:fireworks: **Daily giveaways!** @here
:candy: **Owners/Founders**
<@382582764400148482> - Founder
<@128518520836194314> - Owner
<@358115593343467521> - Owner
<@306036814769291274> - Owner
**--------------------------------------------------------------------------------------**
**Picture:** https://imgur.com/jP7e9JX
**Invite:**  https://discord.gg/a3HDHng```""")
    
@bot.command()
async def owners(ctx):
    await ctx.send("""<@391660447381716992> (Papa)    Owner
<@128518520836194314> (Toby)    Owner
<@358115593343467521> (Arizon)  Owner
<@306036814769291274> (Dutchie)    Owner
<@188614474167484416> (Smoke)   Co-Owner
<@385132387404742657> (Support) Co-Owner""")
    
@bot.command()
async def staffapp(ctx):
    await ctx.send("https://docs.google.com/forms/d/e/1FAIpQLScgADh0gT1lgFDGMp_PflW49_QTRwq-RfibysIlypOUNnd30g/viewform")
    
@bot.command()
async def movies(ctx):
    await ctx.send("""So you typed in this command thinking that it'll play a movie that's where you are wrong
so this command is here to tell you about out movie nights which will now be every Friday night if you want to
suggest a movie to us or find out more about this dm/pm <@188614474167484416> and when you suggested a movie it'll be added to
the suggest command type suggestions to see all of  our current suggestions of that week.""")
    
@bot.command()
async def games(ctx):
    await ctx.send("""This ain't no game command! No it's information about our games event which will be on every Saturday evening where
we will all play a game of your choice as a community, the way the games will be decided is similar to above basically dm/pm <@188614474167484416>
of the game you want to play and then by Friday we'll know what games we going to play which would be top 3most suggested
again your suggestions will be in suggestions command""")
    
@bot.command()
async def suggestions(ctx):
    await ctx.send("""**__Wonder__** = Movie


**__Suggestions info__**= Every Friday we'll go through them and the ones with most votes will be the movie/game we'll play/watch
also if the movie you suggested is already apart of the suggestions then we'll add a number next to that movie/game to show
that this amount  of ppl voted for it.""")
    
@bot.command()
async def help(ctx):
    await ctx.send("""```css
**Bot Commands**
• Nhelp (Displays this message)
• Nbotspurpose
• Nbotowner
• Nserverinv
• Npartnerinfo
• Nowners
• Nstaffapp (stafff application)
• Nmovies
• Ngames
• Nsuggestions```""")

bot.run("process.env.BOT_TOKEN")
