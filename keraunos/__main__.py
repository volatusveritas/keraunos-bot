from os import getenv

from discord.ext import commands

from keraunos import console
from keraunos import constants
from keraunos.keep_alive import keep_alive


EXTLIST: list = [
]


class Keraunos(commands.Bot):
    def run(self) -> None:
        console.dbprint("Initializing Keraunos...")
        super().run(getenv("TOKEN"))

    async def on_ready(self) -> None:
        console.dbprint("Keraunos is logged in, with bot state:")
        console.bot_state(self)


bot: Keraunos = Keraunos(command_prefix="kn.")


@bot.command()
async def reload(ctx):
    if (ctx.author.id != constants.ENGINEER_ID):
        await ctx.channel.send(
            "Não és o engenheiro. Somente ele pode usar este comando."
        )
        return

    await ctx.channel.send("Keraunos está sendo reiniciado.")

    for ext in EXTLIST:
        bot.reload_extension(ext)


keep_alive()
bot.run()
