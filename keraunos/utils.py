import discord

from keraunos import constants


async def send_embed(ctx, title, message, colorname="neutral"):
    embed = discord.Embed(
        title=title,
        description=message,
        color=constants.COLORS[colorname],
    )

    await ctx.send(embed=embed)


async def send_error(ctx, message):
    await send_embed(ctx, "Erro", message, "critical")
