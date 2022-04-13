from os import getenv

from discord.ext import commands

from keraunos import console
from keraunos import constants
from keraunos.keep_alive import keep_alive


ext_list: list = list(constants.EXTENSIONS)


class Keraunos(commands.Bot):
    def run(self) -> None:
        console.dbprint("Initializing Keraunos...")
        super().run(getenv("TOKEN"))

    async def on_ready(self) -> None:
        console.dbprint("Keraunos is logged in, with bot state:")
        console.bot_state(self)


bot: Keraunos = Keraunos(command_prefix="kn.")


async def engineer_check(ctx):
    if ctx.author.id != constants.ENGINEER_ID:
        await ctx.channel.send(
            "Não és o Engenheiro. Somente ele pode usar este comando."
        )
        return False

    return True


@bot.command()
async def e_reload(ctx):
    if not await engineer_check(ctx):
        return

    await ctx.channel.send("Keraunos está sendo reiniciado.")

    for ext in ext_list:
        bot.reload_extension(ext)


@bot.command()
async def e_listext(ctx):
    if not await engineer_check(ctx):
        return

    await ctx.channel.send(f"Lista de extensões: {', '.join(ext_list)}")


keep_alive()
bot.run()
