import discord
from discord.ext import commands
import nest_asyncio
import random

#prefix changeable here  
client = commands.Bot(command_prefix='+')
client.remove_command('help')

@client.command(aliases=['BB11', 'Bb11', 'bB11'])
async def bb11(ctx):
    embed = discord.Embed(
        title = 'BB11 is a clown!',
        description = 'BB11 is a booster, DC glicher, and walks from 1v1s. He has failed 5 Top 3 grinds and talks shit about everyone.' ,
        color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Clown_emoji_grande.png?v=1513251032")
    embed.set_footer(text="BB11=CLOWN")
    await ctx.send(embed=embed)
 



    
 

#bot invite command
@client.command(aliases=['invite_bot', 'Invite', 'invite me', 'invite_btd battles_bot'])
async def invite(ctx):
    embed = discord.Embed(
        title = 'Invite BTD Battles Bot to your own discord server!',
        description = 'Click [here](https://discord.com/api/oauth2/authorize?client_id=763531402712317962&permissions=8&scope=bot) to see the invite link for BTD Battles Bot' ,
        color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://th.bing.com/th/id/OIP.zB1J1YA-FUGm2LVfRkMWdQHaHa?pid=Api&rs=1")
    embed.set_footer(text="Stuck? Join my support server at discord.gg/e8bUfYQ")
    await ctx.send(embed=embed)
 

#faq command
@client.command(aliases=['FAQ', 'Faq', 'FAq', 'fAq', 'faqs'])
async def faq(ctx):
    embed = discord.Embed(
        title = 'FAQs for BTD Battles Bot',
        description = 'Please go to #faqs (if it exists in your server) or click [here](https://docs.google.com/document/d/1dQPpQWe1cRvz8IKSuAxhgPeXUUwmwTBoxxamddohmaQ/edit?usp=sharing) to see the FAQs online' ,
        color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://customclinichq.com/wp-content/uploads/2017/04/frequently-asked-questions.jpg")
    embed.set_footer(text="If you see any bugs, wrong information, or have questions join the support server at discord.gg/e8bUfYQ")
    await ctx.send(embed=embed)
    
#support server command    
@client.command(aliases=['Support'])
async def support(ctx):
    embed = discord.Embed(
        title = 'Support Server for BTD Battles Bot',
        description = 'Need Support? Click [here](https://discord.com/invite/e8bUfYQ) to join' ,
        color = discord.Colour.green(),
    )
    embed.set_thumbnail(url="https://community.telligent.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-17-78/support.jpg")
    embed.set_footer(text="Link not work? Copy and paste this into your browser. discord.gg/e8bUfYQ")
    await ctx.send(embed=embed)

   
#help command    
@client.command(aliases=['Help', 'commands', 'command', ])
async def help(ctx):
    embed = discord.Embed(
        title = 'Help for BTD Battles Bot',
        description = 'Need help? Click [here](https://docs.google.com/document/d/1fLQk_21bFSLV3fqcqhDBiQmMPfxTaC7k4xU_BXe4qpo/edit?usp=sharing) to view the commands.' ,
        color = discord.Colour.green(),
    )
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/R8JPK1ntZDcEol95b5ao0RTwfJppA72whu8Rwr_btEM/http/img.talkandroid.com/uploads/2014/06/help.jpg?width=450&height=450")
    embed.set_footer(text="Still stuck? Join my support server at discord.gg/e8bUfYQ")
    await ctx.send(embed=embed)
#END Of Settings commands    

    
#Tower COMMANdS below     
#dart monkey 0-0
@client.command(aliases=['Dart'])
async def dart(ctx):
    embed = discord.Embed(
        title = 'Dart Monkey',
        description = 'Cost = $200, The dart monkey is one of a kind. This beast is good early game with the triple dart (0-3) and the powerful fan club. Also is good for the best known strat, Dart Farm Ace! \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
        color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://i.imgur.com/JniOVYF.png")
    await ctx.send(embed=embed)
    
    
#dart monkey 0-1   
@client.command(aliases=['Dart01', 'dart11', 'Dart11', 'Dart21', 'dart21'])
async def dart01(ctx):
    embed = discord.Embed(title = 'Sharp Shots 0-1', description = 'Cost = $340 (total), This is simply a 0-0 dart monkey ($200) with sharp shots. It pops two ballons at once instead of one, so increasing the pierce to 2. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server' , color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/b__/images/9/92/100-Dartmonkey.png/revision/latest?cb=20190522024645&path-prefix=bloons")
    await ctx.send(embed=embed)
    
#dart monkey 0-2
@client.command(aliases=['Dart02','dart22', 'dart12', 'Dart22', 'Dart12'])
async def dart02(ctx):
    embed = discord.Embed(title = 'Razar Sharp Darts 0-2', description = 'Cost = $510 (total), This is simply a 0-0 dart monkey ($200) with sharp shots & Razor Sharp Shots. It pops two more ballons at once instead of one, so increasing the pierce to 4. This is also the upgrade before the triple dart \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server' , color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/b__/images/e/e0/200-Dartmonkey.png/revision/latest/scale-to-width-down/619?cb=20190522025041&path-prefix=bloons")
    await ctx.send(embed=embed)
    
#dart monkeyy 0-3
@client.command(aliases=['Dart03', 'dart23', 'dart13', 'Dart23', 'Dart13'])
async def dart03(ctx):
    embed = discord.Embed(title = 'Triple Darts 0-3', description = 'Cost = $840 (total), This dart monkey is the best at poping ballons when spammed and just a very good defense tower. It is very good early game and is the best comboed with spult (3-0) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server' , color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/b__/images/b/bb/Triple_Darts_Monkey.png/revision/latest?cb=20180720024036&path-prefix=bloons")
    await ctx.send(embed=embed)
 
#dart monkey 0-4
@client.command(aliases=['Dart04', 'dart24', 'Dart24', 'dart14', 'Dart14'])
async def dart04(ctx):
    embed = discord.Embed(title = 'Super Monkey Fan Club 0-4', description = 'Cost = $8840 (total), This dart monkey is the best at poping MOAB Class Ballons. When you use the ability ten (10) nearby darts will transform into mini super monkeys. This is very powerful. If you upgrade the nearby darts to at least 0-2 they will recive more pierce and do more damage. This ability cannot be spammed. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server' , color = discord.Colour.green(),)                   
    embed.set_thumbnail(url= "https://vignette.wikia.nocookie.net/b__/images/1/1b/Super_Monkey_Fan_Club_Monkey.png/revision/latest?cb=20180720030424&path-prefix=bloons")
    await ctx.send(embed=embed)
    
@client.command(aliases=['Dart10'])
async def dart10(ctx):
    embed = discord.Embed(title = 'Long Range Darts 1-0', description = 'Cost = $290 (total), This is a plain 0-0 dart (1 piecre) with a boost of range \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server', 
    color = discord.Colour.green(),)
    embed.set_thumbnail(url= "https://vignette.wikia.nocookie.net/b__/images/8/8f/001-Dartmonkey.png/revision/latest?cb=20190522015551&path-prefix=bloons")
    await ctx.send(embed=embed)
    
    
    

@client.command(aliases=['Dart20'])
async def dart20(ctx):
    embed = discord.Embed(title = 'Enchanced Eyesight 2-0', description = 'Cost = $410 (total), This is a plain 0-0 dart (1 piecre) with a extra boost of range. It does not give any extra pierce only range. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server', 
    color = discord.Colour.green(),)
    embed.set_thumbnail(url= "https://vignette.wikia.nocookie.net/b__/images/d/d0/Enhanced_Eyesight_Monkey.png/revision/latest?cb=20180720202206&path-prefix=bloons")
    await ctx.send(embed=embed)
    
@client.command(aliases=['Dart30', 'dart31', 'dart32', 'Dart31', 'Dart32'])
async def dart30(ctx):
    embed = discord.Embed(title = 'Spike-a-Pult 3-0', description = 'Cost = $2810 (total), This upgrade is a very very powerful upgrade. The right side does not change anything (does not even change piecre) so its a waste of money. This is best at all kinds of rushes and ceramices. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server ',
    color = discord.Colour.green(),)
    embed.set_thumbnail(url= "https://vignette.wikia.nocookie.net/b__/images/1/11/300-Dartmonkey.png/revision/latest?cb=20190522025343&path-prefix=bloons")
    await ctx.send(embed=embed)
    
@client.command(aliases=['Dart40','dart42', 'dart41', 'Dart41', 'Dart42'])
async def dart40(ctx):
    embed = discord.Embed(title = 'Juggernaut 4-0', description = 'Cost = $910 (total), This upgrade is a very powerful upgrade. The right side does not change anything (does not even change piecre) so its a waste of money. This is very powerful agaist all ballons even ceramics. This means it is a great counter to cobra. This will shread the cermic layer like its nothing \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server!', 
    color = discord.Colour.green(),)
    embed.set_thumbnail(url= "https://vignette.wikia.nocookie.net/b__/images/8/8a/Juggernaut.jpg/revision/latest?cb=20150204224443&path-prefix=bloons")
    await ctx.send(embed=embed)
    
#dart is done
#start of tack shooter

#0-0 tack
@client.command(aliases=['Tack','tack shooter', 'Tack Shooter'])
async def tack(ctx):
    embed = discord.Embed(
        title = 'Tack Shooter',
        description = 'Cost = $360, The tack shooter is a very special tower. This tower is not a monkey! This tower is good when upgraded to the blade malstorm (0-4) or just the 2-3 blade shooter. It is very good early game. The best placement is if you can get the path or ballons to go around it. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
        color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/b__/images/4/4c/HD_Fix_Tack_Shooter.png/revision/latest?cb=20151222214112&path-prefix=bloons")
    await ctx.send(embed=embed)
  

#0-1 tack
@client.command(aliases=['Tack01'])
async def tack01(ctx):
    embed = discord.Embed(
        title = 'Extra Range Tacks 0-1',
        description = 'Cost = $450, This is just a plain 0-0 tack with a small boost of range. Range is very little on tack shooters so this is a good upgrade comboed with a left side upgrade but is very bad by itself. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
        color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/b__/images/c/c4/Extrarangetacksteam.png/revision/latest?cb=20181225053130&path-prefix=bloons")
    await ctx.send(embed=embed)

#0-2 tack 
@client.command(aliases=['Tack02'])
async def tack02(ctx):
    embed = discord.Embed(
        title = 'Super Range Tacks 0-2',
        description = 'Cost = $560, This is just a plain 0-0 tack with a extra boost of range. Range is very little on tack shooters so this is a good upgrade comboed with a left side upgrade but is very bad by itself. This upgrade is right before the blade shooter which is very good early game. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
        color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/b__/images/8/87/BMC_0-2_Tack_Shooter.png/revision/latest?cb=20200328235904&path-prefix=bloons")
    await ctx.send(embed=embed)
    

#0-3 tack

@client.command(aliases=['Tack03'])
async def tack03(ctx):
    embed = discord.Embed(
        title = 'Blade Shooter 0-3',
        description = 'Cost = $1160, This upgrade is a beast. If you properly place this it will solo the first 10 rounds if you upgrade to the left side by two. This will tear apart most rushes and is one of the best early game towers. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/b__/images/7/73/Bladeshooter5.PNG/revision/latest?cb=20161229082839&path-prefix=bloons")
    await ctx.send(embed=embed)
    

#0-4 tack
@client.command(aliases=['Tack04'])
async def tack04(ctx):
    embed = discord.Embed(
        title = 'Blade Malstorm 0-4',
        description = 'Cost = $3960, This upgrade is the best at defending non-camo rushes and MOABs. This ability will clear the screen and two of these will destory a moab. This is one of the best abilities in the game. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/b__/images/9/98/Maelstrom_Official_Artwork.png/revision/latest?cb=20121122223044&path-prefix=bloons")
    await ctx.send(embed=embed)
    
#I just finished the right side of tack

@client.command(aliases=['Tack10'])
async def tack10(ctx):
    embed = discord.Embed(
        title = 'Faster Shooting 1-0',
        description = 'Cost = $570, This tack shooter is a 0-0 tack with a slight boost of attck speed. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/btd-5/images/3/3c/Tack_Shooter.png/revision/latest?cb=20130201231454")
    await ctx.send(embed=embed)
    

@client.command(aliases=['Tack20'])
async def tack20(ctx):
    embed = discord.Embed(
        title = 'Even Faster Shooting 2-0',
        description = 'Cost = $920, This tack shooter can shoot quite fast but does not have good piecre. This upgrade is best comboed with the blade shooter (2-3) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/764195307213815808/764630396415246336/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['Tack30'])
async def tack30(ctx):
    embed = discord.Embed(
        title = 'Tack Sprayer 3-0',
        description = 'Cost = $1420, This tack shooter is best agaist moabs and not good early game. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/764195307213815808/764630396415246336/unknown.png")
    await ctx.send(embed=embed)
    




    


    
    

    
    

    
    
    
#maps

@client.command(aliases=['Offside'])
async def offside(ctx):
    embed = discord.Embed(
        title = 'Offside',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/743967963178336348/764687434256482364/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['Snowy Castle','snowy castle'])
async def castle(ctx):
    embed = discord.Embed(
        title = 'Snowy Castle',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764688669025501234/unknown.png")
    await ctx.send(embed=embed)

@client.command(aliases=['Interchange'])
async def interchange(ctx):
    embed = discord.Embed(
        title = 'Interchange',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764688712973680640/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['concrete alley','alley'])
async def concretealley(ctx):
    embed = discord.Embed(
        title = 'Concrete Alley',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764688749199228968/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['swan lake', 'Swan'])
async def swanlake(ctx):
    embed = discord.Embed(
        title = 'Swan Lake',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764688788319895632/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['Mondrain'])
async def mondrain(ctx):
    embed = discord.Embed(
        title = 'Mondrain',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764688848839507968/unknown.png")
    await ctx.send(embed=embed)
    
    
@client.command(aliases=['bloon circles'])
async def blooncircles(ctx):
    embed = discord.Embed(
        title = 'Bloon Circles',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764689937198743572/unknown.png")
    await ctx.send(embed=embed)
    

@client.command(aliases=['ink blot'])
async def inkblot(ctx):
    embed = discord.Embed(
        title = 'Ink Blot',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764689982337187840/unknown.png")
    await ctx.send(embed=embed)   
 
@client.command(aliases=['blast', 'blastapopulos'])
async def Blastapopulos(ctx):
    embed = discord.Embed(
        title = 'Blastapopulos',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764690026717118514/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['Bloonarius'])
async def bloonarius(ctx):
    embed = discord.Embed(
        title = 'Blastapopulos',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764690049912406026/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['Dreadbloon', 'Dreadbloon Cave'])
async def dreadbloon(ctx):
    embed = discord.Embed(
        title = 'Dreadbloon Cave',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764690097866014730/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['Vortex'])
async def vortex(ctx):
    embed = discord.Embed(
        title = 'Vortex',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764695500141887488/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['tub', 'hot tub'])
async def hottub(ctx):
    embed = discord.Embed(
        title = 'Hot Tub',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764695536459710464/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['zen', 'zen garden', 'Zen'])
async def zengarden(ctx):
    embed = discord.Embed(
        title = 'Zen Garden',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764695651078242304/unknown.png")
    await ctx.send(embed=embed)

@client.command(aliases=['Inlets'])
async def inlets(ctx):
    embed = discord.Embed(
        title = 'Inlets',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764695699501350912/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['ghostly', 'ghostly coast'])
async def ghostlycoast(ctx):
    embed = discord.Embed(
        title = 'Ghostly Coast',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764696540018901002/unknown.png")
    await ctx.send(embed=embed)
    
    
@client.command(aliases=['wizards keep', "wizard's keep", "Wizard's Keep"])
async def wizardskeep(ctx):
    embed = discord.Embed(
        title = "Wizard's Keep",
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764696589141803018/unknown.png")
    await ctx.send(embed=embed)
    
    
@client.command(aliases=['SML', 'super monkey lane', 'Super Monkey Lane'])
async def sml(ctx):
    embed = discord.Embed(
        title = 'Super Monkey Lane',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764696630594502678/unknown.png")
    await ctx.send(embed=embed)
    

                         
@client.command(aliases=['Area52', 'Area 52', 'area 52'])
async def area52(ctx):
    embed = discord.Embed(
        title = 'Area 52',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764696753127161856/unknown.png")
    await ctx.send(embed=embed)
                         
@client.command(aliases=['wattle resorts', 'wattle', 'Wattle'])
async def wattleresorts(ctx):
    embed = discord.Embed(
        title = 'Wattle Resorts',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764696833263796254/unknown.png")
    await ctx.send(embed=embed)
    
@client.command(aliases=['Roadblock'])
async def roadblock(ctx):
    embed = discord.Embed(
        title = 'Roadblock',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764696878607499274/unknown.png")
    await ctx.send(embed=embed)
                         
@client.command(aliases=['Riverside'])
async def riverside(ctx):
    embed = discord.Embed(
        title = 'Riverside',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764698566178242560/unknown.png")
    await ctx.send(embed=embed)

                         
@client.command(aliases=['space station'])
async def spacestation(ctx):
    embed = discord.Embed(
        title = 'Space Startion',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764698615708516392/unknown.png")
    await ctx.send(embed=embed)

@client.command(aliases=['mountain pass', 'Mountain Pass'])
async def mountainpass(ctx):
    embed = discord.Embed(
        title = 'Mountain Pass',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764698655516000276/unknown.png")
    await ctx.send(embed=embed)
                         
                         
@client.command(aliases=['industrial zone'])
async def industrialzone(ctx):
    embed = discord.Embed(
        title = 'Industrial Zone',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764698792691105823/unknown.png")
    await ctx.send(embed=embed)
                         
@client.command(aliases=['frozen river'])
async def frozenriver(ctx):
    embed = discord.Embed(
        title = 'Frozen River',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764698828976291880/unknown.png")
    await ctx.send(embed=embed)
                         
                         
                         
@client.command(aliases=['shallow river'])
async def shallowriver(ctx):
    embed = discord.Embed(
        title = 'Shallow River',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764698866770771998/unknown.png")
    await ctx.send(embed=embed)
                         
                         
@client.command(aliases=['moon Llanding'])
async def moonlanding(ctx):
    embed = discord.Embed(
        title = 'Moon Landing',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764698905756958730/unknown.png")
    await ctx.send(embed=embed)
                         
                    
@client.command(aliases=['Shapes'])
async def shapes(ctx):
    embed = discord.Embed(
        title = 'Shapes',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764698938934558730/unknown.png")
    await ctx.send(embed=embed)

                         
@client.command(aliases=['pinball wizard', 'Pinball', 'pinball'])
async def pinballwizard(ctx):
    embed = discord.Embed(
        title = 'Pinball Wizard',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764698982164987925/unknown.png")
    await ctx.send(embed=embed)   
                         
                         
                         
@client.command(aliases=['treasure hunt', 'treasure'])
async def treasurehunt(ctx):
    embed = discord.Embed(
        title = 'Treasure Hunt',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699004894183444/unknown.png")
    await ctx.send(embed=embed) 
                         
                         
@client.command(aliases=['Cards'])
async def cards(ctx):
    embed = discord.Embed(
        title = 'Cards',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699034677805096/unknown.png")
    await ctx.send(embed=embed) 

@client.command(aliases=['race track'])
async def racetrack(ctx):
    embed = discord.Embed(
        title = 'Race Track',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699069989781534/unknown.png")
    await ctx.send(embed=embed) 
                         
@client.command(aliases=['Mine'])
async def mine(ctx):
    embed = discord.Embed(
        title = 'Mine',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699103744884746/unknown.png")
    await ctx.send(embed=embed) 
 
                         
@client.command(aliases=['Park'])
async def park(ctx):
    embed = discord.Embed(
        title = 'Park',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699138884370452/unknown.png")
    await ctx.send(embed=embed) 
                         
@client.command(aliases=['Temple'])
async def temple(ctx):
    embed = discord.Embed(
        title = 'Inlets',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699172045455360/unknown.png")
    await ctx.send(embed=embed) 
                         
                         
@client.command(aliases=['yang yang'])
async def yingyang(ctx):
    embed = discord.Embed(
        title = 'Ying Yand',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699241196027934/unknown.png")
    await ctx.send(embed=embed)                          
                         
                         
@client.command(aliases=['hydro', 'hydro dam'])
async def hydrodam(ctx):
    embed = discord.Embed(
        title = 'Hydro Dam',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699271416643605/unknown.png")
    await ctx.send(embed=embed)                          
                         
                         
@client.command(aliases=['battle park'])
async def battlepark(ctx):
    embed = discord.Embed(
        title = 'Battle Park',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699312101130281/unknown.png")
    await ctx.send(embed=embed)                          
                         
@client.command(aliases=['battle river'])
async def battleriver(ctx):
    embed = discord.Embed(
        title = 'Battle River',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699343609266196/unknown.png")
    await ctx.send(embed=embed)                          
                         
                         
@client.command(aliases=['battle sands', 'Pyramid Steps', 'pyramid steps'])
async def battlesands(ctx):
    embed = discord.Embed(
        title = 'Battle Sands',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699375066677268/unknown.png")
    await ctx.send(embed=embed)                          
                         
                        
 
@client.command(aliases=['ybr', 'yellow brick road', 'YBR', 'yellow dick road'])
async def yellowbrickroad(ctx):
    embed = discord.Embed(
        title = 'Yellow Brick Road',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699402916724746/unknown.png")
    await ctx.send(embed=embed)                          

                         
@client.command(aliases=['Swamp'])
async def swamp(ctx):
    embed = discord.Embed(
        title = 'Swamp',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764699432079065128/unknown.png")
    await ctx.send(embed=embed) 
                         
@client.command(aliases=['Patch'])
async def patch(ctx):
    embed = discord.Embed(
        title = 'Patch',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764703581734961152/unknown.png")
    await ctx.send(embed=embed) 
                         
                         
@client.command(aliases=['Snowfall'])
async def snowfall(ctx):
    embed = discord.Embed(
        title = 'Snowfall',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764703581734961152/unknown.png")
    await ctx.send(embed=embed) 
                         
                         
                         
@client.command(aliases=['water hazard'])
async def waterhazard(ctx):
    embed = discord.Embed(
        title = 'Water Hazard',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764703660746997760/unknown.png")
    await ctx.send(embed=embed) 
                         
                         
@client.command(aliases=['a game'])
async def agame(ctx):
    embed = discord.Embed(
        title = 'A Game',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764703738920960010/unknown.png")
    await ctx.send(embed=embed) 
                         
                         
@client.command(aliases=['indoor pools', 'pools', 'Pools'])
async def indoorpools(ctx):
    embed = discord.Embed(
        title = 'Indoor Pools',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764703889869504532/unknown.png")
    await ctx.send(embed=embed) 
                         
                         
@client.command(aliases=['ice flow'])
async def iceflow(ctx):
    embed = discord.Embed(
        title = 'Ice Flow',
        description = '\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764703927962042418/unknown.png")
    await ctx.send(embed=embed)                          
                         

####
####
####
####











####btd emotes

@client.command(aliases=['SWAG', 'Swag'])
async def swag(ctx):
    embed = discord.Embed(
        title = 'Swag - BTD Emote',
        description = 'BTD Battles Emote \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/750116046806974465.gif?v=1")
    await ctx.send(embed=embed)         
        
        
@client.command(aliases=['crying', 'CRY', 'Cry', 'Sad', 'sad', 'SAD'])
async def cry(ctx):
    embed = discord.Embed(
        title = 'Sad - BTD Emote',
        description = 'BTD Battles Emote \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/695819602378096761.png?v=1")
    await ctx.send(embed=embed)  
    
    
@client.command(aliases=['Facepalm'])
async def facepalm(ctx):
    embed = discord.Embed(
        title = 'Facepalm - BTD Emote',
        description = 'BTD Battles Emote \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/695819349671542824.png?v=1")
    await ctx.send(embed=embed)  
    
    
@client.command(aliases=['Thumbsup'])
async def thumbsup(ctx):
    embed = discord.Embed(
        title = 'Thumbsup - BTD Emote',
        description = 'BTD Battles Emote \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/738753909782478911.png?v=1")
    await ctx.send(embed=embed)  
    
@client.command(aliases=['Thumbsdown'])
async def thumbsdown(ctx):
    embed = discord.Embed(
        title = 'Thumbsdown - BTD Emote',
        description = 'BTD Battles Emote \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/761663912659386428.png?v=1")
    await ctx.send(embed=embed)  
    
 
    
@client.command(aliases=['Angry', 'Pissed', 'pissed'])
async def angry(ctx):
    embed = discord.Embed(
        title = 'Angry - BTD Emote',
        description = 'BTD Battles Emote \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/761664140862554152.png?v=1")
    await ctx.send(embed=embed)  
        

@client.command(aliases=['Shocked'])
async def shocked(ctx):
    embed = discord.Embed(
        title = 'Shocked - BTD Emote',
        description = 'BTD Battles Emote \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/761664175658893343.png?v=1")
    await ctx.send(embed=embed) 
    
    
@client.command(aliases=['LMAO', 'Lmao', 'laughing', 'Laughing'])
async def lmao(ctx):
    embed = discord.Embed(
        title = 'Laughing - BTD Emote',
        description = 'BTD Battles Emote \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/738753909610250262.png?v=1")
    await ctx.send(embed=embed) 
                
        
 
##### btd battles powers track





########################################################################



















@client.command(aliases=['TowerBoost'])
async def towerboost(ctx):
    embed = discord.Embed(
        title = 'Tower Boost - BTD Power',
        description = 'In game description: Boosts your Towers attack speed by 80% for 12 seconds. Three uses. \n XP Needed to abtain: 0xp (You get this for starting the game) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764887025538695199/unknown.png")
    await ctx.send(embed=embed)


@client.command(aliases=['RangeBoost'])
async def rangeboost(ctx):
    embed = discord.Embed(
        title = 'Range Boost - BTD Power',
        description = 'In game description: Boosts your Towers range by 60% and attck speed by 50% for 20 seconds. Three uses. \n XP needed to abtain: (total) 500 \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764888264405680148/unknown.png")
    await ctx.send(embed=embed)
    
    
@client.command(aliases=['CamoShread'])
async def camoshread(ctx):
    embed = discord.Embed(
        title = 'Camo Shread - BTD Power',
        description = 'In game description: Boosts attack speed and enables towers to see and do more damage to camo bloons for 20 seconds. Three uses. \n XP needed to abtain: (total) 3000 \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764888619231477780/unknown.png")
    await ctx.send(embed=embed)
    
    
@client.command(aliases=['PopBoost'])
async def popboost(ctx):
    embed = discord.Embed(
        title = 'Pop Boost - BTD Power',
        description = 'In game description: Boosts attack speed and enables towers to see and do more damage to camo bloons for 20 seconds. Three uses. \n XP Needed to Abtain: (total) 8000xp \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764888660549042186/unknown.png")
    await ctx.send(embed=embed)


@client.command(aliases=['DamageBoost'])
async def damageboost(ctx):
    embed = discord.Embed(
        title = 'Damage Boost - BTD Power',
        description = 'In game description: Pop two layers for the price of one. All towers get +1 damage and slight attck speed boost for 18 seconds. Three uses. \n XP needed to abtain: (total) 15500 \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764888785334173756/unknown.png")
    await ctx.send(embed=embed)
        
        
@client.command(aliases=['ImprovedTowerBoost'])
async def improvedtowerboost(ctx):
    embed = discord.Embed(
        title = 'Improved Tower Boost - BTD Power',
        description = 'In game description: Boost you towers attack speed by 100% for 10 seconds. Three uses. \n XP needed to abtain:(total) 500 \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764905868524912660/unknown.png")
    await ctx.send(embed=embed)        
        
        
        
@client.command(aliases=['Long Tower Boost'])
async def longtowerboost(ctx):
    embed = discord.Embed(
        title = 'Long Tower Boost - BTD Power',
        description = 'In game description: Boost your Towers attack speed by 60% for 20 seconds. Three uses. \n XP needed to abtain:(total) 3000 \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764905814628368434/unknown.png")
    await ctx.send(embed=embed)        
        
        
        
        
        
@client.command(aliases=['IntenseTowerBoost'])
async def intensetowerboost(ctx):
    embed = discord.Embed(
        title = 'Intense Tower Boost - BTD Power',
        description = 'In game description: A quick but extreme boost for your towers. Attack speed increased by 110% for 9 seconds. Three uses. \n XP needed to abtain:(total) 8000 \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764905935784247306/unknown.png")
    await ctx.send(embed=embed)        
        
        
        
        
@client.command(aliases=['EmpoweredTowers'])
async def empoweredtowers(ctx):
    embed = discord.Embed(
        title = 'Empowered Towers - BTD Power',
        description = 'In game description: Boost your Towers attack speed by 85% and range by 20% for 16 seconds. Three uses. \n XP Needed to abtain: (total) 15500\n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764905968562995241/unknown.png")
    await ctx.send(embed=embed)        
        
        
        
@client.command(aliases=['BigBloonBeatdown', 'bbb1'])
async def bigbloonbeatdown(ctx):
    embed = discord.Embed(
        title = 'Big Bloon Beatdown - BTD Power',
        description = 'In game description: Towers do double damage to MOAB-Class bloons for 22 seconds. Four uses. \n XP needed to abtain: 500 (total) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764905997025148948/unknown.png")
    await ctx.send(embed=embed)        
        

@client.command(aliases=['BigBloonBuster', 'bbb2'])
async def bigbloonbuster(ctx):
    embed = discord.Embed(
        title = 'Big Bloon Buster - BTD Power',
        description = 'In game description: Towers do triple damage to MOAB-Class bloons for 18 seconds. Three uses. \n XP needed to abtain: (total) 3000 \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764906033415323648/unknown.png")
    await ctx.send(embed=embed)     
    
    
@client.command(aliases=['BigBloonSlow', 'bbs'])
async def bigbloonslow(ctx):
    embed = discord.Embed(
        title = 'Big Bloon Slow - BTD Power',
        description = 'In game description: All MOAB-Class bloons move 60% slower for 15 seconds. Three uses. \n XP needed to abtain: (total) 8000 \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764906060574097418/unknown.png")
    await ctx.send(embed=embed) 
        
@client.command(aliases=['BloonSnipe'])
async def bloonsnipe(ctx):
    embed = discord.Embed(
        title = 'Bloon Snipe - BTD Power',
        description = 'In game description: Instantly destory the largest Bloon on screen. Five uses. \n XP needed to abtain: 15500  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764906112725811200/unknown.png")
    await ctx.send(embed=embed)         
        
        

        
        
    
        
        
               
      
#Powers Templete        
#@client.command(aliases=[''])
#async def (ctx):
#    embed = discord.Embed(
#        title = ' - BTD Power',
#        description = 'In game description:  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
#    color = discord.Colour.green(),)
#    embed.set_thumbnail(url="")
#    await ctx.send(embed=embed)           
        
        
@client.command(aliases=['RedHotSpikes', 'RoadSpikes', 'roadspikes'])
async def redhotspikes(ctx):
    embed = discord.Embed(
        title = 'Red Hot Spikes - BTD Power',
        description = 'In game description: Place a bundle of 30 red hot spikes. Three uses. \n XP needed to abtain: 0 (You get this for starting the game) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764914111917064212/unknown.png")
    await ctx.send(embed=embed)  

@client.command(aliases=['BetterBundles'])
async def betterbundles(ctx):
    embed = discord.Embed(
        title = 'Better Bundles - BTD Power',
        description = 'In game description: Place a bundle of 23 red hot spikes. Three uses. \n XP needed to abtain: 500 (total) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764914167488053268/unknown.png")
    await ctx.send(embed=embed) 
    
    
@client.command(aliases=['EvenBetterBundles'])
async def evenbetterbundles(ctx):
    embed = discord.Embed(
        title = 'Even Better Bundles - BTD Power',
        description = 'In game description: Place a bundle of 25 red hot spikes. Three uses. \n XP needed to abtain: 3000 (total) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764914192146235452/unknown.png")
    await ctx.send(embed=embed) 

    
@client.command(aliases=['BestBundles'])
async def bestbundles(ctx):
    embed = discord.Embed(
        title = 'Best Bundles - BTD Power',
        description = 'In game description: Place a bundle of 30 red hot spikes. Three uses. \n XP needed to abtain: 8000  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764914339752575007/unknown.png")
    await ctx.send(embed=embed) 

    
@client.command(aliases=['SpikeStorm'])
async def spikestorm(ctx):
    embed = discord.Embed(
        title = 'Spike Storm - BTD Power',
        description = 'In game description: Cover the entire track in red hot spikes. Two uses. \n XP needed to abtain: 15500 (total) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764914275718004736/unknown.png")
    await ctx.send(embed=embed) 


@client.command(aliases=['MonkeyGlue'])
async def monekyglue(ctx):
    embed = discord.Embed(
        title = 'Moneky Glue - BTD Power',
        description = 'In game description: Place a blob of corrosive glue on the track. Three uses. \n XP needed to abtain: 500 (total)  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764916194562015252/unknown.png")
    await ctx.send(embed=embed) 

@client.command(aliases=['LotsOfGlue'])
async def lotsofglue(ctx):
    embed = discord.Embed(
        title = 'Lots of Glue - BTD Power',
        description = 'In game description: Place a bigger blob of regular glue (not corrosive) on the track. Five uses. \n XP needed to abtain: 3000 (total)  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764916231873626182/unknown.png")
    await ctx.send(embed=embed) 
    
    
@client.command(aliases=['Monkey Acid', 'Acid', 'ACID', 'acid'])
async def monkeyacid(ctx):
    embed = discord.Embed(
        title = 'Monkey Acid - BTD Power',
        description = 'In game description: Place a blob of bloon dissolver glue on the track. Three uses. \n XP needed to abtain: 8000 (total)  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764916256335593492/unknown.png")
    await ctx.send(embed=embed) 
    
    
@client.command(aliases=['GlueStorm'])
async def gluestorm(ctx):
    embed = discord.Embed(
        title = 'Glue Storm - BTD Power',
        description = 'In game description: Cover all the bloons on screen in corrosive glue continuously for 4 seconds. Three uses. \n XP needed to abtain: 15500 (total)  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764916285304733696/unknown.png")
    await ctx.send(embed=embed) 
    
    
@client.command(aliases=['ExplodingMegaPineapples', 'Pineapples', 'pineapples'])
async def explodingmegapineapples(ctx):
    embed = discord.Embed(
        title = 'Exploding Mega Pineapples- BTD Power',
        description = 'In game description: Drop a large exploding pineapple on the track to deal with groups of bloons. Fifteen uses. \n XP needed to abtain: 500 (total) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764918367097585714/unknown.png")
    await ctx.send(embed=embed) 
    
    
@client.command(aliases=['LightningBolts', 'lightning', 'Lightning'])
async def lightningbolts(ctx):
    embed = discord.Embed(
        title = 'Lightning Bolts - BTD Power',
        description = 'In game description: Place a lightning tower to strike out at bloons on the screen. Three uses. \n XP needed to abtain: 3000 (total)  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764918401721565214/unknown.png")
    await ctx.send(embed=embed) 

@client.command(aliases=['Juggerlanche'])
async def juggerlanche(ctx):
    embed = discord.Embed(
        title = 'Juggerlanche - BTD Power',
        description = 'In game description: An avalanche of Juggernauts roll down the screen wiping out any bloons. Two uses. \n XP needed to abtain: 8000 (total) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764918429730865192/unknown.png")
    await ctx.send(embed=embed) 
    

@client.command(aliases=['Shield'])
async def shield(ctx):
    embed = discord.Embed(
        title = 'Shield - BTD Power',
        description = 'In game description: A shield blocks the exit, stopping 150 red bloons, or equivalent, from leaking. One use. \n XP needed to abtain: 15500 (total)   \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764918481908662322/unknown.png")
    await ctx.send(embed=embed) 
    
    



@client.command(aliases=['BloonBoost'])
async def bloonboost(ctx):
    embed = discord.Embed(
        title = 'Bloon Boost - BTD Power',
        description = 'In game description: Speed up spawned bloons by 30% for 12 seconds. Three uses. \n XP needed to abtain: 0 (You get this for starting the game)   \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764953613696499712/unknown.png")
    await ctx.send(embed=embed) 
    

@client.command(aliases=['CrowdedBloons'])
async def crowdedbloons(ctx):
    embed = discord.Embed(
        title = 'Crowded Bloons - BTD Power',
        description = 'In game description: Increase the spawn rate of bloons by 50% for 15 seconds. Three uses. \n XP needed to abtain: 500 (total)   \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764953668034101298/unknown.png")
    await ctx.send(embed=embed) 
    

@client.command(aliases=['JamPacked'])
async def jampacked(ctx):
    embed = discord.Embed(
        title = 'Jam Packed - BTD Power',
        description = 'In game description: Bloons move 15% faster and spawn twice as fast for 10 seconds. Two uses. \n XP needed to abtain: 3000 (total)   \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764953720160387092/unknown.png")
    await ctx.send(embed=embed) 
    


@client.command(aliases=['Upgrade Bloons'])
async def upgradebloons(ctx):
    embed = discord.Embed(
        title = 'Upgrade Bloons - BTD Power',
        description = 'In game description: Increases by one rank the next 15 bloons spawned, up to a maximum of Rainbow. Three uses. \n XP needed to abtain: 8000 (total) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764953796106387516/unknown.png")
    await ctx.send(embed=embed) 
        
    
@client.command(aliases=['CamoRegrowEfficiency'])
async def camoregrowefficiency(ctx):
    embed = discord.Embed(
        title = 'Camo Regrow Efficiency - BTD Power',
        description = 'In game description: The cost of Camo and regrow upgrades are reduced by 25% for 15 seconds. Three uses. \n XP Needed to abtain: 15500 (total) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764953836619563028/unknown.png")
    await ctx.send(embed=embed) 
        
    
    
@client.command(aliases=['ImprovedBloonBoost'])
async def improvedbloonboost(ctx):
    embed = discord.Embed(
        title = 'Improved Bloon Boost - BTD Power',
        description = 'Speed up send bloons by 40% for 12 seconds. Three uses. \n XP needed to abtain: 500  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764956346951925780/unknown.png")
    await ctx.send(embed=embed) 
        
    
    
    
@client.command(aliases=['Quickshot', 'QuickShot'])
async def quickshot(ctx):
    embed = discord.Embed(
        title = 'Quick Shot - BTD Power',
        description = 'In game description: Speed up next 8 sent non-MOAB class bloons for 100%. Three uses. \n XP needed to abtain: 3000 (total) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764956379944452116/unknown.png")
    await ctx.send(embed=embed) 
        
    
    
    
@client.command(aliases=['LongBloonBoost'])
async def longbloonboost(ctx):
    embed = discord.Embed(
        title = 'Long Bloon Boost - BTD Power',
        description = 'In game description: Speed up sent bloons by 25% for 20 seconds. Three uses. \n XP needed to abtain: 8000 (total)  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764956418205024276/unknown.png")
    await ctx.send(embed=embed) 
        
    
    
@client.command(aliases=['SuperBloonBoost'])
async def superbloonboost(ctx):
    embed = discord.Embed(
        title = 'Super Bloon Boost - BTD Power',
        description = 'In game description: Bloons reach super speed. Sent bloons move 50% faster for 10 seconds. Three uses. \n XP needed to abtain: 15500 (total) \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764956463918743572/unknown.png")
    await ctx.send(embed=embed) 
        
    
@client.command(aliases=['MoabBoost'])
async def moabboost(ctx):
    embed = discord.Embed(
        title = 'Moab Boost - BTD Power',
        description = 'In game description: Speed up sent MOAB-class bloons by 50% for 15 seconds. Three uses. \n XP needed to abtain: 500 (total)  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764956495652716545/unknown.png")
    await ctx.send(embed=embed) 
            
    
@client.command(aliases=['BeefyMoabs', 'beefymoab', 'BeefyMoab'])
async def beefymoabs(ctx):
    embed = discord.Embed(
        title = 'Beefy Moabs - BTD Power',
        description = 'In game description: Increase health of send MOAB-class bloons by 50% for 20 seconds. Three uses. \n XP Needed to abtain: 3000 (total)  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764956527860645918/unknown.png")
    await ctx.send(embed=embed) 
               
    
@client.command(aliases=['TurboMoabs', 'TurboMoab', 'turbomoab'])
async def turbomoabs(ctx):
    embed = discord.Embed(
        title = 'Turbo Moabs - BTD Power',
        description = 'In game description: Speed up next 2 MOAB-class bloons by 60% for 20 seconds. Three uses. \n XP Needed to abtain: 8000 (total)  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764956557116309505/unknown.png")
    await ctx.send(embed=embed) 
                
    
@client.command(aliases=['EmpoweredMoabs', 'EmpoweredMoab', 'empoweredmoab'])
async def empoweredmoabs(ctx):
    embed = discord.Embed(
        title = 'Empowered Moabs - BTD Power',
        description = 'In game description: Increase health by 30% and speed by 30% of sent MOAB-class bloons for 15 seconds. Three uses. \n XP needed to abtain: 15500 (total)  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764956582802751558/unknown.png")
    await ctx.send(embed=embed) 
                
    
    
    
    
    
    
    
    
#@client.command(aliases=[''])
#async def (ctx):
#    embed = discord.Embed(
#    title = ' - BTD Power',
#        description = 'In game description:  \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
#    color = discord.Colour.green(),)
#    embed.set_thumbnail(url="")
#    await ctx.send(embed=embed)     
    
    
@client.command(aliases=['Powers', 'power', 'Power'])
async def powers(ctx):
    embed = discord.Embed(
    title = 'BTD Battles Powers',
        description = '**What category of powers do you want to know?** \n \n Track \n Tower \n Bloon \n Eco \n Sabo \n \n Type +{category} \n Currently Only Track, Tower and Bloon categories work. \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/764960462512848976/unknown.png")
    await ctx.send(embed=embed)        
    
@client.command(aliases=['Track'])
async def track(ctx):
    embed = discord.Embed(
    title = 'BTD Battles Track Powers:',
        description = 'List all track powers (do +{power name without spaces} to see even MORE information): \n \n Red Hot Spikes, Better Bundles, Even Better Bundles, Best Bundles, Spike Storm \n Monkey Glue, Lots of Glue, Monkey Acid, Glue Storm \n Exploding Mega Pineapples, Lightning Bolts, Juggerlanche, Shield \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/765052301752664084/unknown.png")
    await ctx.send(embed=embed)  
    
    
@client.command(aliases=['Tower'])
async def tower(ctx):
    embed = discord.Embed(
    title = 'BTD Battles Tower Powers:',
        description = 'List all tower powers (do +{power name without spaces} to see even MORE information): \n \n Tower Boost, Range Boost, Camo Shread, Pop Boost, Damage Boost \n Improved Tower Boost, Long Tower Boost, Intense Tower Boost, Empowered Towers \n Big Bloon Beatdown, Big Bloon Buster, Big Bloon Slow, Bloon Snipe \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/765052194872623124/unknown.png")
    await ctx.send(embed=embed) 
    
    
@client.command(aliases=['Bloon'])
async def bloon(ctx):
    embed = discord.Embed(
    title = 'BTD Battles Bloon Powers:',
        description = 'List all bloon powers (do +{power name without spaces} to see even MORE information): \n \n Bloon Boost, Crowded Bloons, Jam Packed, Upgrade Bloons, Camo Regrow Efficiency \n Improved Bloon Boost, Quick Shot, Long Bloon Boost, Super Bloon Boost \n Moab Boost, Beefy Moabs, Turbo Moabs, Empowered Moabs \n \n If you see any bugs, wrong information, or have questions click [here](https://discord.com/invite/e8bUfYQ) to join the support server.' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764685871982575676/765052242831081492/unknown.png")
    await ctx.send(embed=embed) 
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


  
        
        
        
        
        
        
        
        
        
        
# paid persons or people/ btd lengels or just very important people below #

@client.command(aliases=['EliteGodNL', 'Jimmy', 'jimmy'])
async def elitegodnl(ctx):
    embed = discord.Embed(
        title = 'EliteGodNL ',
        description = 'What the actual fuck do you want me to put here?' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="http://clipart-library.com/images/BcaEg6bzi.png")
    await ctx.send(embed=embed)   


@client.command(aliases=['Ninjayas', 'NINJAYAS'])
async def ninjayas(ctx):
    embed = discord.Embed(
        title = 'Ninjayas the legendary grinder ',
        description = 'What the actual fuck do you want me to put here?' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="http://clipart-library.com/images/BcaEg6bzi.png")
    await ctx.send(embed=embed) 
        

@client.command(aliases=['Division', 'DIV', 'Div'])
async def division(ctx):        
    embed = discord.Embed(
        title = 'Join Division the official T1 Bloons TD Battles Clan!',
        description = 'Click [here](https://discord.gg/Dc2ZgEM) to see the invite link for Division' ,
    color = discord.Colour.green(),)
    embed.set_thumbnail(url="https://bit.ly/33SroIu")
    await ctx.send(embed=embed)        
        
@client.command(aliases=['Potg', 'POTG'])
async def potg(ctx):         
    embed = discord.Embed(
        title = 'Join Pantheon Of The Gods a Bloons TD Battles Clan!',
        description = 'Click [here](https://discord.gg/EnQPevF) to see the invite link for Pantheon Of The Gods' ,
        color = discord.Colour.green(),)
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/739402496622985257/765662314593648700/695821374379261952.png")
    embed.set_footer(text="Stuck? Join our support server at discord.gg/e8bUfYQ")
    await ctx.send(embed=embed)        
        
        
        
        
        
        
        
        
        
        
        
        
        
#status and ready up message   
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='+support | +help'))
    print("BTD Battles Bot is ready and online on discord. Version 0.87.1v")                        
                         
                         
                                           
                         
                         
                                                  
                         
#If you are make crosspaths use the aliases to make unless the crosspath is very very different

client.run('NzYzNTMxNDAyNzEyMzE3OTYy.X35ECA.jG7cC_HwGJD-fSFEtdCWX04A0aY') 
#bot token do not change this!
