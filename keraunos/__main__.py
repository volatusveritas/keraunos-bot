from os import getenv
import configparser

from discord.ext import commands

from keraunos import utils
from keraunos.keep_alive import keep_alive
from keraunos.log import logger, setup_logging


setup_logging()


class Keraunos(commands.Bot):
    def run(self):
        self.config_init()
        super().run(getenv("TOKEN"))

    def config_init(self):
        self.config = configparser.ConfigParser()
        self.config.read_file(open("keraunos.conf"))

        for ext in self.config["keraunos.init"]["extensions"].split(","):
            self.load_extension(f"keraunos.extensions.{ext}")

    async def on_connect(self):
        logger.info("Bot connected")

    async def on_ready(self):
        logger.info("Bot ready to receive commands")

    async def on_disconnect(self):
        logger.info("Bot disconnected")

    async def on_command_error(self, ctx, ex):
        if isinstance(ex, commands.CommandNotFound):
            await utils.send_error(
                ctx, "Comando não encontrado ou indisponível."
            )
        else:
            raise ex


bot = Keraunos(("keraunos.", "krns.", "kn.", "{",))

keep_alive()
bot.run()
