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
            await ctx.send("Comando não encontrado ou indisponível.")


bot: Keraunos = Keraunos(command_prefix=("keraunos.", "kn.", "{",))


async def engineer_check(ctx) -> bool:
    if ctx.author.id != constants.ENGINEER_ID:
        await ctx.send(
            "Não és o Engenheiro. Somente ele pode usar este comando."
        )
        return False

    return True


@bot.command()
async def e_reload(ctx, *args) -> None:
    if not await engineer_check(ctx):
        return

    if not args:
        await ctx.send("Uso: `e_reload (all | {<extensão>})`")
        return

    exts_to_reload = []

    if args[0] != "all":
        await ctx.send(f"Reiniciando extensões: {', '.join(args)}.")
        exts_to_reload = args
    else:
        if not bot.extensions.keys():
            await ctx.send("Nenhuma extensão a ser recarregada.")
            return

        await ctx.send("Recarregando todas as extensões.")
        exts_to_reload = list(bot.extensions.keys())

    for ext in exts_to_reload:
        try:
            bot.reload_extension(f"keraunos.extensions.{ext}")
            await ctx.send(f"Extensão recarregada: {ext}")
        except commands.ExtensionNotFound:
            await ctx.send(f"Extensão '{ext}' não encontrada.")
        except commands.ExtensionNotLoaded:
            await ctx.send(f"Extensão '{ext}' não carregada.")


@bot.command()
async def e_list(ctx) -> None:
    if not await engineer_check(ctx):
        return

    if bot.extensions:
        await ctx.send(
            "Lista de extensões carregadas:"
            f" {', '.join(bot.extensions.keys())}."
        )
    else:
        await ctx.send("Não existem extensões carregadas.")


@bot.command()
async def e_load(ctx, *args) -> None:
    if not await engineer_check(ctx):
        return

    if not args:
        await ctx.send("Uso: `load {<extensão>}`.")
        return

    await ctx.send(f"Carregando extensões: {', '.join(args)}")

    for ext in args:
        try:
            bot.load_extension(f"keraunos.extensions.{ext}")
            await ctx.send(f"Extensão carregada: {ext}.")
        except commands.ExtensionAlreadyLoaded:
            await ctx.send(f"Extensão '{ext}' já carregada.")
        except commands.ExtensionNotFound:
            await ctx.send(f"Extensão '{ext}' não encontrada.")


@bot.command()
async def e_unload(ctx, *args) -> None:
    if not await engineer_check(ctx):
        return

    if not args:
        await ctx.send("Uso: `unload {<extensão>}`.")
        return

    await ctx.send(f"Descarregando extensões: {', '.join(args)}")

    for ext in args:
        try:
            bot.unload_extension(f"keraunos.extensions.{ext}")
            await ctx.send(f"Extensão descarregada: {ext}.")
        except commands.ExtensionNotFound:
            await ctx.send(f"Extensão '{ext}' não encontrada.")
        except commands.ExtensionNotLoaded:
            await ctx.send(f"Extensão '{ext}' não carregada.")


keep_alive()
bot.run()
