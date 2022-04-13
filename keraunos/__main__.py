from os import getenv

import discord

from keraunos import console
from keraunos.keep_alive import keep_alive


class KeraunosClient(discord.Client):
    def run(self) -> None:
        console.dbprint("Initializing Keraunos...")
        super().run(getenv("TOKEN"))

    async def on_ready(self) -> None:
        console.dbprint("Keraunos is logged in, with bot state:")
        console.bot_state(self)


keraunos_bot: KeraunosClient = KeraunosClient()
keep_alive()
keraunos_bot.run()
