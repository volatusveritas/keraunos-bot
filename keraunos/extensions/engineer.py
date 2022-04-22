from discord.ext import commands

from keraunos import constants
from keraunos import log
from keraunos import utils


class Engineer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def check_permission(self, ctx):
        if (
            ctx.author.id == constants.ENGINEER_ID or
            ctx.author.guild_permissions.administrator
        ):
            return True

        await utils.send_error(
            ctx, "Você não possui permissão para usar esse comando."
        )
        return False

    @commands.command()
    async def e_list(self, ctx):
        if not self.check_permission(ctx):
            return

        message = ""

        for ext in self.bot.extensions:
            message += f"{ext}\n"

        await utils.send_embed(ctx, message, "Engineer: List", "special")

    @commands.command()
    async def e_load(self, ctx, *extensions):
        if not self.check_permission(ctx):
            return

        message = ""

        for ext in extensions:
            try:
                self.bot.load_extension(f"keraunos.extensions.{ext}")
                message += f"`{ext}`: carregada\n"
            except commands.ExtensionNotFound:
                message += f"`{ext}`: não encontrada\n"
            except commands.ExtensionAlreadyLoaded:
                message += f"`{ext}`: já carregada\n"

        await utils.send_embed(ctx, message, "Engineer: Load", "special")

    @commands.command()
    async def e_unload(self, ctx, *extensions):
        if not self.check_permission(ctx):
            return

        message = ""

        for ext in extensions:
            try:
                self.bot.unload_extension(f"keraunos.extensions.{ext}")
                message += f"`{ext}`: descarregada\n"
            except commands.ExtensionNotFound:
                message += f"`{ext}`: não encontrada\n"
            except commands.ExtensionNotLoaded:
                message += f"`{ext}`: não estava carregada\n"

        await utils.send_embed(ctx, message, "Engineer: Unload", "special")

    @commands.command()
    async def e_reload(self, ctx, *extensions):
        if not self.check_permission(ctx):
            return

        message = ""

        for ext in extensions:
            try:
                self.bot.reload_extension(f"keraunos.extensions.{ext}")
                message += f"`{ext}`: recarregada\n"
            except commands.ExtensionNotFound:
                message += f"`{ext}`: não encontrada\n"
            except commands.ExtensionNotLoaded:
                message += f"`{ext}`: não estava carregada\n"

        await utils.send_embed(ctx, message, "Engineer: Reload", "special")


def setup(bot):
    bot.add_cog(Engineer(bot))
    log.extension_loaded("engineer")


def teardown(bot):
    bot.remove_cog("Engineer")
    log.extension_unloaded("engineer")
