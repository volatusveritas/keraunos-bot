from os import getenv

from discord.ext import commands

from keraunos import console
from keraunos import constants
from keraunos.keep_alive import keep_alive


class Keraunos(commands.Bot):
    def run(self) -> None:
        console.dbprint("Initializing Keraunos...")
        super().run(getenv("TOKEN"))

    async def on_ready(self) -> None:
        console.dbprint("Keraunos is logged in, with bot state:")
        console.bot_state(self)

    async def on_command_error(self, ctx, ex) -> None:
        try:
            raise ex
        except commands.CommandNotFound:
            await ctx.channel.send("Comando não encontrado ou indisponível.")


bot: Keraunos = Keraunos(command_prefix=(
    "{",
    "kn.",
))


async def engineer_check(ctx) -> bool:
    if ctx.author.id != constants.ENGINEER_ID:
        await ctx.channel.send(
            "Não és o Engenheiro. Somente ele pode usar este comando."
        )
        return False

    return True


@bot.command()
async def e_reload(ctx, *args) -> None:
    if not await engineer_check(ctx):
        return

    if not args:
        await ctx.channel.send("Uso: `e_reload (all | {extensão})`")
        return

    await ctx.channel.send(f"Tentando reiniciar: {', '.join(args)}")

    for ext in args if args[0] != "all" else bot.extensions.keys():
        try:
            bot.reload_extension(ext)
        except commands.ExtensionNotFound:
            await ctx.channel.send(f"Extensão '{ext}' não encontrada.")
        except commands.ExtensionNotLoaded:
            await ctx.channel.send(f"Extensão '{ext}' não carregada.")


@bot.command()
async def e_list(ctx) -> None:
    if not await engineer_check(ctx):
        return

    if bot.extensions:
        await ctx.channel.send(
            f"Lista de extensões: {', '.join(bot.extensions.keys())}."
        )
    else:
        await ctx.channel.send("Não existem extensões carregadas.")


@bot.command()
async def e_load(ctx, *args) -> None:
    if not await engineer_check(ctx):
        return

    if not args:
        await ctx.channel.send("Uso: `load {extensão}`.")
        return

    await ctx.channel.send(f"Tentando adicionar: {', '.join(args)}")

    for ext in args:
        try:
            bot.load_extension(ext)
        except commands.ExtensionAlreadyLoaded:
            ctx.channel.send(f"Extensão '{ext}' já carregada.")
        except commands.ExtensionNotFound:
            ctx.channel.send(f"Extensão '{ext}' não encontrada.")


@bot.command()
async def e_unload(ctx, *args) -> None:
    if not await engineer_check(ctx):
        return

    if not args:
        await ctx.channel.send("Uso: `unload {extensão}`.")
        return

    await ctx.channel.send(f"Tentando remover: {', '.join(args)}")

    for ext in args:
        try:
            bot.unload_extension(ext)
        except commands.ExtensionNotFound:
            ctx.channel.send(f"Extensão '{ext}' não encontrada.")
        except commands.ExtensionNotLoaded:
            ctx.channel.send(f"Extensão '{ext}' não carregada.")


keep_alive()
bot.run()
