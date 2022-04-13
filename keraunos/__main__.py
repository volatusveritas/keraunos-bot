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


bot: Keraunos = Keraunos(command_prefix=(
    "{",
    "kn.",
    "krns "
    "keraunos ",
))


async def engineer_check(ctx):
    if ctx.author.id != constants.ENGINEER_ID:
        await ctx.channel.send(
            "Não és o Engenheiro. Somente ele pode usar este comando."
        )
        return False

    return True


@bot.command()
async def e_reload(ctx, *args):
    if not await engineer_check(ctx):
        return

    await ctx.channel.send(f"Tentando reiniciar: {', '.join(args)}")

    for ext in args:
        bot.reload_extension(ext)


@bot.command()
async def e_reloadall(ctx):
    if not await engineer_check(ctx):
        return

    await ctx.channel.send("Reiniciando todas as extensões.")

    for ext in ext_list:
        bot.reload_extension(ext)


@bot.command()
async def e_list(ctx):
    if not await engineer_check(ctx):
        return

    if ext_list:
        await ctx.channel.send(f"Lista de extensões: {', '.join(ext_list)}.")
    else:
        await ctx.channel.send("Não existem extensões ativadas.")


@bot.command()
async def e_add(ctx, *args):
    if not await engineer_check(ctx):
        return

    await ctx.channel.send(f"Tentando adicionar: {', '.join(args)}")

    for ext in args:
        ext_list.remove(ext)


@bot.command()
async def e_remove(ctx, *args):
    if not await engineer_check(ctx):
        return

    await ctx.channel.send(f"Tentando remover: {', '.join(args)}")

    for ext in args:
        ext_list.append(ext)


@bot.command()
async def e_reset(ctx):
    global ext_list

    await ctx.channel.send("Redefinindo a lista de extensões.")

    if not await engineer_check(ctx):
        return

    ext_list = list(constants.EXTENSIONS)


keep_alive()
bot.run()
