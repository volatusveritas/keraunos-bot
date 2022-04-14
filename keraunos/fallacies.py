from discord.ext import commands


@commands.group(
    name="fallacy", aliases=("fal", "f"), invoke_without_command=True
)
async def fallacy(ctx):
    await ctx.send("Subcomando inválido.")


@fallacy.group(name="define", aliases=("def", "d"))
async def fallacy_define(ctx):
    await ctx.send(
        "O termo **falácia** deriva do verbo latino *fallere*, que significa"
        "enganar. Designa-se por falácia um raciocínio errado com aparência de"
        "verdadeiro. Na lógica e na retórica, uma falácia é um argumento"
        "logicamente incoerente, sem fundamento, inválido ou falho na"
        "tentativa de provar eficazmente o que alega. Argumentos que se"
        "destinam à persuasão podem parecer convincentes para grande parte do"
        "público apesar de conterem falácias, mas não deixam de ser falsos por"
        "causa disso."
    )


def setup(bot: commands.Bot) -> None:
    bot.add_command(fallacy)
    bot.add_command(fallacy_define)
