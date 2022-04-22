from os import getenv
from configparser import ConfigParser

from discord.ext import commands

from keraunos.keep_alive import keep_alive
from keraunos.log import logger, setup_logging


setup_logging()


class Keraunos(commands.Bot):
    def run(self):
        self.config_init()
        super().run(getenv("TOKEN"))

    def config_init(self):
        self.config = ConfigParser()
        self.config.read("keraunos.conf")

        for ext in self.config["keraunos.init"]["extensions"].split(","):
            self.load_extension(f"keraunos.extensions.{ext}")

    async def on_connect(self):
        logger.info("Bot connected")

    async def on_ready(self):
        logger.info("Bot ready to receive commands")

    async def on_disconnect(self):
        logger.info("Bot disconnected")

    async def on_command_error(self, ctx, ex):
        try:
            raise ex
        except commands.CommandNotFound:
            await ctx.send("Comando não encontrado ou indisponível.")


bot = Keraunos(("keraunos.", "krns.", "kn.", "{",))

keep_alive()
bot.run()
