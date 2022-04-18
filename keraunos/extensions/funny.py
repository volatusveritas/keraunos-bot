from discord.ext import commands


@commands.group()
async def funny(ctx):
    await ctx.send("Subcomando inválido.")


@funny.group()
async def funny_meyer(ctx):
    await ctx.send(
        "Olá! Chamo-me Carlos Ernesto de Boaventura Meyer, sou seminarista,"
        " estudante de filosofia, teologia e linguística. Futuro Padre, estudo"
        " também história, falante nativo de Português, vivo na Região"
        " Sul-Fluminense, onde atuo na Administração Apostólica São João Maria"
        " Vianney. Estudo Italiano, Latim e Francês - se Deus quiser - Grego e"
        " Hunsriqueano Rio-Grandense. Aristotélico, distributivista e tomista."
        "Para aqueles que estiverem lendo a respeito de minha pessoa, Deus vos"
        " abençoe! AD MAJOREM DEI GLORIAM!"
    )
