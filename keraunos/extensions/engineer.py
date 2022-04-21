from discord.ext import commands

from keraunos import log


class Engineer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Engineer(bot))
    log.extension_loaded("engineer")


def teardown(bot):
    bot.remove_cog("Engineer")
    log.extension_unloaded("engineer")
