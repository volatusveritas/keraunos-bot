import discord

from keraunos import constants


async def send_embed(ctx, title: str, message: str) -> None:
    embed = discord.Embed(
        title=title, description=message, color=constants.KERAUNOS_COLOR
    )
    await ctx.send(embed=embed)
