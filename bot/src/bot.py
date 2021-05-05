from discord.ext import commands

bot = commands.Bot(command_prefix="-")

@bot.command
async def ping(ctx: commands.Context):
    await ctx.send("pong")

@bot.event
async def on_ready():
    print("Logged in as {}".format(bot.user.name))
