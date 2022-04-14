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
        " enganar. Designa-se por falácia um raciocínio errado com aparência"
        " de verdadeiro. Na lógica e na retórica, uma falácia é um argumento"
        " logicamente incoerente, sem fundamento, inválido ou falho na"
        " tentativa de provar eficazmente o que alega. Argumentos que se"
        " destinam à persuasão podem parecer convincentes para grande parte do"
        " público apesar de conterem falácias, mas não deixam de ser falsos"
        " por causa disso."
    )


@fallacy.group(name="probability", aliases=("prob", "atp"))
async def fallacy_appeal_to_probability(ctx):
    await ctx.send(
        "Um **apelo à probabilidade** (ou **apelo à possibilidade**, também"
        "conhecido como *possibiliter ergo probabiliter*, \"possivelmente,"
        "portanto provavelmente\") é a falácia lógica de tomar algo como"
        "certo porque provavelmente seria o caso (ou talvez poderia ser o"
        "caso). Argumentos indutivos carecem de validade dedutiva e devem,"
        "portanto, ser afirmados ou negados nas premissas. Uma mera"
        "possibilidade não se correlaciona com uma probabilidade, e uma mera"
        "probabilidade não se correlaciona com uma certeza, nem é apenas"
        "qualquer probabilidade de que algo aconteceu ou acontecerá suficiente"
        "para qualificar como saber que aconteceu ou acontecerá.\""
    )


def setup(bot: commands.Bot) -> None:
    bot.add_command(fallacy)
    bot.add_command(fallacy_define)
