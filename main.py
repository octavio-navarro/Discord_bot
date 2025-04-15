import os

import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


class Client(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents, **kwargs):
        super().__init__(command_prefix, intents=intents, **kwargs)

    async def on_ready(self):
        await self.change_presence(
            status=discord.Status.online, activity=discord.Game(name="Neovim")
        )

        cog_list = ["cogs.greetings"]

        for cog in cog_list:
            try:
                cog_name = cog.split(".")[-1]
                await bot.load_extension(cog)
                print(f"Succesfully loaded module {cog_name}")
            except Exception as e:
                print(f"Error loading cog: {cog} - {e}")

        await bot.tree.sync()

        print("Cogs loades succesfully")


if __name__ == "__main__":
    bot = Client(command_prefix="!", intents=discord.Intents.default())
    bot.run(TOKEN)
