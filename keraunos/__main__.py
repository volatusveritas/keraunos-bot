from os import getenv

from discord.ext import commands

from keraunos.keep_alive import keep_alive
from keraunos.log import logger, setup_logging


setup_logging()


class Keraunos(commands.Bot):
    def run(self):
        # (temporary) manually load extensions
        bot.load_extension("keraunos.extensions.engineer")
        bot.load_extension("keraunos.extensions.fallacies")
        bot.load_extension("keraunos.extensions.funny")

        super().run(getenv("TOKEN"))

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
