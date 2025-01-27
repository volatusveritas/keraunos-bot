from discord.ext import commands

from keraunos import utils
from keraunos import log


class Fallacies(commands.Cog):
    @commands.group(aliases=("fal", "f"), invoke_without_command=True)
    async def fallacy(self, ctx):
        await utils.send_error(ctx, "Subcomando inválido.")


    @fallacy.group(name="list", aliases=("ls", "l"))
    async def fallacy_list(self, ctx):
        list = (
            "Apelo à probabilidade: `probability | prob | atp`\n"
            "Apelo à falácia: `fallacy | fal | aff`\n"
            "Non sequitur: `sequitur | seq | ns`\n"
            "Ad hominem: `hominem | hom | ah`\n"
            "Ad ignorantiam: `ignorantiam | ign | ai`\n"
            "Ad trollum: `trollum | troll | tr`\n"
        )

        await utils.send_embed(ctx, list, "Lista de falácias disponíveis")


    @fallacy.group(name="define", aliases=("def", "d"))
    async def fallacy_define(self, ctx):
        definition = (
            "O termo **falácia** deriva do verbo latino *fallere*, que significa"
            " enganar. Designa-se por falácia um raciocínio errado com aparência"
            " de verdadeiro. Na lógica e na retórica, uma falácia é um argumento"
            " logicamente incoerente, sem fundamento, inválido ou falho na"
            " tentativa de provar eficazmente o que alega. Argumentos que se"
            " destinam à persuasão podem parecer convincentes para grande parte do"
            " público apesar de conterem falácias, mas não deixam de ser falsos"
            " por causa disso."
        )

        await utils.send_embed(ctx, definition, "Definição de falácia")


    @fallacy.group(name="probability", aliases=("prob", "atp"))
    async def fallacy_appeal_to_probability(self, ctx):
        definition = (
            "Um **apelo à probabilidade** (ou **apelo à possibilidade**, também"
            " conhecido como *possibiliter ergo probabiliter*, \"possivelmente,"
            " portanto provavelmente\") é a falácia lógica de tomar algo como"
            " certo porque provavelmente seria o caso (ou talvez poderia ser o"
            " caso)."
        )

        await utils.send_embed(ctx, definition, "Apelo à probabilidade")


    @fallacy.group(name="fallacy", aliases=("fal", "aff"))
    async def fallacy_argument_from_fallacy(self, ctx):
        definition = (
            "**Apelo à falácia** é a falácia formal de analisar um argumento e"
            " inferir que, já que este contém uma falácia, sua conclusão deve ser"
            " falsa. Também é chamado de **apelo à lógica** (***argumentum ad"
            " logicam***), **falácia da falácia**, e **falácia das más razões**."
        )

        await utils.send_embed(ctx, definition, "Apelo à falácia")


    @fallacy.group(name="sequitur", aliases=("seq", "ns"))
    async def fallacy_non_sequitur(self, ctx):
        definition = (
            "**Non sequitur** é uma expressão do latim (traduzida para o português"
            " como \"não se segue que\") que designa a falácia lógica na qual a"
            " conclusão não decorre das premissas. Em um *non sequitur*, a"
            " conclusão pode ser verdadeira ou falsa, mas o argumento é falacioso"
            " porque há falta de conexão entre a premissa inicial e a conclusão."
        )

        await utils.send_embed(ctx, definition, "Non sequitur")


    @fallacy.group(name="hominem", aliases=("hom", "ah"))
    async def fallacy_ad_hominem(self, ctx):
        definition = (
            "**Argumentum ad hominem** (latim, \"argumento contra a pessoa\") é"
            " uma falácia informal identificada quando alguém procura negar uma"
            " proposição com uma crítica ao seu autor e não ao seu conteúdo."
        )

        await utils.send_embed(ctx, definition, "Ad hominem")


    @fallacy.group(name="ignorantiam", aliases=("ign", "ai"))
    async def fallacy_ad_ignorantiam(self, ctx):
        definition = (
            "**Argumentum ad ignorantiam** (em português: argumento da ignorância,"
            " também referida como apelo à ignorância) designa uma falácia lógica"
            " que tenta provar que algo é falso ou verdadeiro a partir de uma"
            " ignorância anterior sobre o assunto. É um tipo de falso dilema, já"
            " que assume que todas as premissas são verdadeiras ou que todas as"
            " premissas serão falsas."
        )

        await utils.send_embed(ctx, definition, "Ad ignorantiam")


    @fallacy.group(name="trollum", aliases=("troll", "tr"))
    async def fallacy_ad_trollum(self, ctx):
        definition = (
            "**Argumentum ad trollum** (latim, \"argumento do troll\") designa"
            " uma falácia retórica na qual um discursista inicia um debate ou"
            " emite uma opinião propositalmente errada ou calculadamente contrária"
            " com o único intuito de trazer outro discursista para uma armadilha"
            " de humor"
        )

        await utils.send_embed(ctx, definition, "Ad trollum")


def setup(bot):
    bot.add_cog(Fallacies())
    log.extension_loaded("fallacies")


def teardown(bot):
    bot.remove_cog("Fallacies")
    log.extension_unloaded("fallacies")
