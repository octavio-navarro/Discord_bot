import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if self.bot.user in message.mentions:
            await message.reply(f"{message.author} please don't ping me")


async def setup(bot: commands.Bot):
    await bot.add_cog(Greetings(bot))
