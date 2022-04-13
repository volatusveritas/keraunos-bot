from os import getenv

import discord

from keraunos import console


class KeraunosClient(discord.Client):
    def run(self) -> None:
        console.dbprint("Initializing Keraunos...")
        super().run(getenv("TOKEN"))

    async def on_ready(self) -> None:
        console.dbprint("Keraunos is logged in, with bot state:")
        console.bot_state(self)


keraunos_bot: KeraunosClient = KeraunosClient()
keraunos_bot.run()
