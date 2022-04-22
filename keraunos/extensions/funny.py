from discord.ext import commands

from keraunos import log
from keraunos import utils


class Funny(commands.Cog):
    @commands.group(aliases=("fun", "fn"), invoke_without_command=True)
    async def funny(self, ctx):
        await utils.send_error(ctx, "Subcomando inválido.")


    @funny.group(name="meyer")
    async def funny_meyer(self, ctx):
        await utils.send_embed(ctx, "Carlos Ernesto de Boaventura Meyer",
            "Olá! Chamo-me Carlos Ernesto de Boaventura Meyer, sou seminarista,"
            " estudante de filosofia, teologia e linguística. Futuro Padre, estudo"
            " também história, falante nativo de Português, vivo na Região"
            " Sul-Fluminense, onde atuo na Administração Apostólica São João Maria"
            " Vianney. Estudo Italiano, Latim e Francês - se Deus quiser - Grego e"
            " Hunsriqueano Rio-Grandense. Aristotélico, distributivista e tomista."
            "Para aqueles que estiverem lendo a respeito de minha pessoa, Deus vos"
            " abençoe! AD MAJOREM DEI GLORIAM!"
        )


def setup(bot):
    bot.add_cog(Funny())
    log.extension_loaded("funny")


def teardown(bot):
    bot.remove_cog("Funny")
    log.extension_unloaded("funny")
